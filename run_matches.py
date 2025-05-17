import os
import time
import pathlib

import pynput.keyboard
import pygetwindow
import numpy
import pandas
from AoE2ScenarioParser.datasets.object_support import *

from utils_units import *
from utils_data import *
from utils_scenario import *
from config import *

matchData = loadResults()
matchDataStats = calculateStats(matchData)
matchDataNew = {}

# --------------------------------

def printd(val):
    if debug_print: print("DEBUG:",val)


# --------------------------------

# focus on AoEII window so that keystrokes work
printd("switch to AoE II window")
target_windows = pygetwindow.getWindowsWithTitle("Age of Empires II:")
if target_windows: target_window = target_windows[0]
else: raise Exception("Could not find Age of Empires window")
target_window.activate()
keyboard = pynput.keyboard.Controller()

# setup for xsdat
xsdatfile = folder_xsdat + "/" + name_xs_data
moddate = time.ctime(os.stat(xsdatfile)[8]) # last modified time

# helper function to restart scenario
def restartScenario():
    
    global moddate
    printd("restart match")
    # target_window.activate()
    time.sleep(0.2)
    keyboard.tap(pynput.keyboard.Key.esc)
    time.sleep(0.3)
    keyboard.tap(pynput.keyboard.Key.f10)
    time.sleep(1.5)
    for i in range(6):
        keyboard.tap(pynput.keyboard.Key.tab)
        time.sleep(0.2)
    keyboard.tap(pynput.keyboard.Key.enter)
    time.sleep(0.8)
    keyboard.tap(pynput.keyboard.Key.tab)
    time.sleep(0.2)
    keyboard.tap(pynput.keyboard.Key.enter)
    time.sleep(0.2)
    keyboard.tap(pynput.keyboard.Key.esc)

    # clear xs data file and reset moddate
    printd("clear xsdat file")
    with open(xsdatfile, "wb") as f: pass # clear file
    moddate = time.ctime(os.stat(xsdatfile)[8])

    # wait enough time for the game to restart
    printd("waiting for game to restart")
    time.sleep(8)


printd("getting all match combos")
combo_index = 0
all_combos = []

for c2i in range(len(civ_list)):
    c2 = civ_list[c2i]
    for c3i in range(len(civ_list)):
        if c3i < c2i: continue
        c3 = civ_list[c3i]
        for a2i in range(len(age_list)):
            a2 = age_list[a2i]
            for a3i in range(len(age_list)):
                if a3i < a2i: continue
                a3 = age_list[a3i]

                # no unequal age_list
                if a2i != a3i: continue

                # get list of units for current ages and civs
                units2 = allUnits[c2][a2]
                units3 = allUnits[c3][a3]

                unit_combos = []
                for i2,u2 in enumerate(units2):
                    for i3, u3 in enumerate(units3):

                        # no double counting units
                        if c2i == c3i and a2i == a3i and i3<i2: continue
                        
                        name = getMatchName(a2, a3, c2, c3, u2.ID, u3.ID)
                        num = 0
                        if name in matchDataStats: num = matchDataStats[name][3]

                        unit_combos.append([u2, u3, num])

                all_combos.append([c2, c3, a2, a3, unit_combos])

# helper function to setup the next scenario
def setupNextScenario():
    global combo_index, all_combos, matches_per_scenario, max_repeats, min_repeats, sterr_conv_threshold
                        
    # if all combos completed then go to next combo

    if combo_index >= len(all_combos): 
        printd("there are no remaining scenarios")
        return (0,0,0,0)

    printd("setup next scenario")
    (c2, c3, a2, a3, combo) = all_combos[combo_index]
    completed = True
    for c in combo:

        name = getMatchName(a2, a3, c2, c3, c[0].ID, c[1].ID)
        sterr = 0
        num = 0
        if name in matchDataStats:
            sterr = matchDataStats[name][2]
            num = matchDataStats[name][3]

        if not ((c[2] >= min_repeats and sterr < sterr_conv_threshold) or c[2] >= max_repeats):
            completed = False
            break

    if completed: combo_index += 1

    if combo_index >= len(all_combos): 
        printd("there are no remaining scenarios")
        return (0,0,0,0)

    f = ScenarioMatch()

    # get current combo
    (c2, c3, a2, a3, combo) = all_combos[combo_index]
    f.setupPlayer(1, Civilization.BRITONS, StartingAge.POST_IMPERIAL_AGE)
    f.setupPlayer(2, c2, a2)
    f.setupPlayer(3, c3, a3)

    # get min repeats for each combo
    rcombo = []
    for c in combo:

        # get sterr
        name = getMatchName(a2, a3, c2, c3, c[0].ID, c[1].ID)
        sterr = 0
        stdev = 0
        num = 0
        if name in matchDataStats:
            stdev = matchDataStats[name][1]
            sterr = matchDataStats[name][2]
            num = matchDataStats[name][3]

        # estimate how many more matches of this type
        repA = min_repeats - c[2]
        repB = max_repeats - c[2]
        repC = 1.1*(pow(stdev/sterr_conv_threshold,2)-c[2])

        repeats_left =  min(4*min_repeats,min(repB,max(repA, repC)))
        repeats_left = int(round(repeats_left))

        rcombo.append([repeats_left, c])

    # add all matches in combo until we hit the max
    print("---- repeats-left ----")
    i = 0
    while True:

        rcombo = sorted(rcombo, key=lambda item: -item[0])
        mrep = rcombo[0][0]
        if mrep < 3:
            for r in rcombo: r[0] += 3-mrep

        for p,(repeats_left,c) in enumerate(rcombo):
            # if repeats_left > 0:
            print("- ", c[0].name, c[1].name, repeats_left)
            # create match for each repeat
            for l in range(repeats_left):
                f.createMatch(c[0], c[1], 7, 7, 24, 24)
                c[2] += 1
                i += 1
                if i >= matches_per_scenario: break

            rcombo[p][0] -= int(repeats_left/2)
            if i >= matches_per_scenario: break

        if i >= matches_per_scenario: break

    f.finish()

    # return known data
    return (c2,c3,a2,a3)

# setup the first scenario
(c2_,c3_,a2_,a3_) = setupNextScenario()

# loop over all scenarios
while True:

    # check if there are any matches remaining
    if combo_index >= len(all_combos): 
        print("all matches have been completed")
        break

    # run next scenario and collect constants
    print("running next set of matches")
    restartScenario()
    (c2,c3,a2,a3) = (c2_,c3_,a2_,a3_)
    (c2_,c3_,a2_,a3_) = setupNextScenario()

    # wait until file has been modified
    printd("waiting for xsdata modify")
    while True:
        moddate2 = time.ctime(os.stat(xsdatfile)[8])
        if moddate2 > moddate: break
        time.sleep(0.3)
    time.sleep(1.5) # allow more time for file to be written

    # extract all data from xsdat
    printd("extracting data from xsdat")
    data = []
    with open(xsdatfile, "rb") as f:
        contents = f.read()
        size = len(contents)
        if size == 0: raise Exception("empty xs data file")
        if size % 4 != 0: raise Exception("xs data file size is not a multiple of 4")
        for i in range(0,size,4):
            data.append(int.from_bytes(contents[i:i+4],byteorder="little", signed=True))
 
    # process raw xs data
    printd("process xs data")
    matches = []
    for i in range(0,len(data),sizeMatch):

        m = Match()
        # loaded data
        m.unitId = data[i+0]
        m.hpInitial = data[i+1]
        m.hpFinal = data[i+2]
        m.unitCount = data[i+3]
        m.eunitId = data[i+4]
        m.ehpInitial = data[i+5]
        m.ehpFinal = data[i+6]
        m.eunitCount = data[i+7]
        m.status = data[i+8]
        # constant data
        m.civ = c2
        m.eciv = c3
        m.age = a2
        m.eage = a3

        # only include valid matches
        if m.status >= 3: matches.append(m)

    print("added " + str(len(matches)) + " matches")

    # collect data for each matchup
    for m in matches:
        name = getMatchName(m.age, m.eage, m.civ, m.eciv, m.unitId, m.eunitId)
        if name not in matchDataNew: matchDataNew[name] = []
        matchDataNew[name].append(m)
        if name not in matchData: matchData[name] = []
        matchData[name].append(m)
    
    # calculate stats for each matchup
    matchDataStats = calculateStats(matchData)

    # check if there are any matches remaining
    if combo_index >= len(all_combos): 
        print("all matches have been completed")
        break


# save results to file
saveResults(matchDataNew)

# print results

print("\n\n")
print("hp percent delta [value, stdev, sterr, num-matches]")
for name, stats in matchDataStats.items():

    [mean, std, sterr, count] = stats

    mean = float(mean*100)
    std = float(std*100)
    sterr = float(sterr*100)

    print(name.rjust(40), "%.2f" % mean, "%.2f" % std, "%.2f" % sterr, count)

matchDataStatsSorted = {k: v for k,v in sorted(matchDataStats.items(), key=lambda item: item[1][0])}

# print("\n\n")
# for name, stats in matchDataStatsSorted.items():

#     [mean, std, sterr, count] = stats

#     mean = float(mean*100)
#     std = float(std*100)
#     sterr = float(sterr*100)

#     print(name.rjust(40), "%.2f" % mean, "%.2f" % std, "%.2f" % sterr, count)

pass

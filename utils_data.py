import pathlib
import numpy
from AoE2ScenarioParser.datasets.object_support import *
from AoE2ScenarioParser.datasets.units import *
from config import *
from utils_units import *

# matchData format
# 
# {c2_c3_a2_a3:{u2_u3:{...}]}
# 
# ... = raw, doneCount, count, mean, stdev, sterr, costerr, repeats }
# raw = [ (c2,c3,a2,a3,u2,u3,unitCount,eunitCount,hpInitial,ehpInitial,hpFinal,ehpFinal,status) ]
# 
# doneCount = completed + pending
# count = completed only

# convert the match (civ, age) into unique name
def getMatchNameA(c2,c3,a2,a3):
    return "_".join((str(i) for i in (c2,c3,a2,a3)))

# convert the match (unit) into unique name
def getMatchNameB(u2,u3):
    return "_".join((str(i) for i in (u2,u3)))

# get list of all possible matches based on the setup in config.py
def getAllMatches():

    matches = {}

    for c2 in civ_list:
        c2i = c2.value

        for c3 in civ_list:
            c3i = c3.value
            # no double counting of civs
            if c3i < c2i: continue

            for a2 in age_list:
                a2i = a2.value

                for a3 in age_list:
                    a3i = a3.value

                    # no double counting of ages
                    if c2i == c3i and a3i < a2i: continue

                    # no unequal ages (for now)
                    if a2i != a3i: continue

                    for u2 in allUnits[c2][a2]:
                        u2i = u2.ID
                        for u3 in allUnits[c3][a3]:
                            u3i = u3.ID

                            # no double counting identicle units
                            if c2i == c3i and a2i == a3i and u3i < u2i: continue

                            # todo: more intelligent way to remove identical units
                            # ...

                            # get match names
                            nameA = getMatchNameA(c2i,c3i,a2i,a3i)
                            nameB = getMatchNameB(u2i,u3i)

                            # add the combo
                            if nameA not in matches: matches[nameA] = { }
                            matches[nameA][nameB] = ((c2i,c3i,a2i,a3i,u2i,u3i),{ "raw":[], "fullCount":0, "completedCount":0, "mean":0, "stdev":0, "sterr":0, "costerr":0, "repeats":0 })

    return matches

# update stats for each type of match
def updateStats(matchData):

    for _,dictt in matchData.items():
        for _,(_, data) in dictt.items():
            hpPerDiff = []
            for m in data["raw"]: hpPerDiff.append(m.hpFinal/m.hpInitial - m.ehpFinal/m.ehpInitial)
            data["completedCount"] = len(hpPerDiff)
            if data["completedCount"] == 0: continue
            data["mean"] = numpy.mean(hpPerDiff)
            data["stdev"] = numpy.std(hpPerDiff)
            data["sterr"] = data["stdev"] / numpy.sqrt(data["completedCount"])
            # this is mainly to initialize doneCount
            data["fullCount"] = max(data["fullCount"], data["completedCount"])
            
# write results to file
def saveResults(matchData):

    data_folder = "data/"+game_version+"/matches"
    pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True)

    data_name = user_name + ".csv"
    counter = 0
    while pathlib.Path(data_folder+"/"+data_name).is_file():
        counter += 1
        data_name = user_name + "_" + str(counter) + ".csv"

    with open(data_folder+"/"+data_name, "w") as f:

        for _,dictt in matchData.items():
            for _,(info, data) in dictt.items():
                (c2i,c3i,a2i,a3i,u2i,u3i) = info
                for m in data["raw"]:
                    if not m.new: continue

                    serial_data = (c2i,c3i,a2i,a3i,u2i,u3i, m.unitCount, m.eunitCount,
                                m.hpInitial, m.ehpInitial, m.hpFinal, m.ehpFinal,
                                m.status)
                    
                    for x in serial_data[:-1]: f.write(str(x)+",")
                    for x in serial_data[-1:]: f.write(str(x)+"\n")
        
# load results from files
def loadResults(matchData):

    data_folder = "data/"+game_version+"/matches"
    pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True)

    # loop over all files in directory
    for filename in os.listdir(data_folder):
        if filename.endswith(".csv"):
            with open (os.path.join(data_folder, filename)) as f:
                lines = f.read().split("\n")
                for line in lines:
                    vals = line.split(",")
                    if len(vals) <= 1: continue

                    # parse raw data into match struct
                    m = Match()
                    m.civ = int(vals[0])
                    m.eciv = int(vals[1])
                    m.age = int(vals[2])
                    m.eage = int(vals[3])
                    m.unitId = int(vals[4])
                    m.eunitId = int(vals[5])
                    m.unitCount = int(vals[6])
                    m.eunitCount = int(vals[7])
                    m.hpInitial = int(vals[8])
                    m.ehpInitial = int(vals[9])
                    m.hpFinal = int(vals[10])
                    m.ehpFinal = int(vals[11])
                    m.status = int(vals[12])
                    m.new = False

                    # get names
                    nameA = getMatchNameA(m.civ, m.eciv, m.age, m.eage)
                    nameB = getMatchNameB(m.unitId, m.eunitId)

                    # skip if the match doesn't exist
                    if nameA not in matchData: continue
                    if nameB not in matchData[nameA]: continue

                    # skip if the numbers don't match our settings
                    # ...

                    # add the raw data
                    matchData[nameA][nameB][1]["raw"].append(m)

    # update stats and initialize doneCount
    updateStats(matchData)

# append xsdata into the matchData
def addXSdata(c2, c3, a2, a3, xsdat, matchData):

    # printd("process xs data")

    # process raw xs data into matches
    matches = []
    for i in range(0,len(xsdat),sizeMatch):

        m = Match()
        # loaded data
        m.unitId = xsdat[i+0]
        m.hpInitial = xsdat[i+1]
        m.hpFinal = xsdat[i+2]
        m.unitCount = xsdat[i+3]
        m.eunitId = xsdat[i+4]
        m.ehpInitial = xsdat[i+5]
        m.ehpFinal = xsdat[i+6]
        m.eunitCount = xsdat[i+7]
        m.status = xsdat[i+8]
        # constant data
        m.civ = c2
        m.eciv = c3
        m.age = a2
        m.eage = a3
        m.new = True

        # only include valid matches
        if m.status >= 3: matches.append(m)

    print("added " + str(len(matches)) + " matches")

    # collect data for each matchup
    for m in matches:
        nameA = getMatchNameA(m.civ, m.eciv, m.age, m.eage)
        nameB = getMatchNameB(m.unitId, m.eunitId)

        # don't check if the counts are reasonable; just assume they are
        # ...

        # just assume the name is in matchData; as it should be
        # ...

        matchData[nameA][nameB][1]["raw"].append(m)

    # update stats
    updateStats(matchData)

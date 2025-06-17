from AoE2ScenarioParser.datasets.object_support import *

from utils_units import *
from utils_data import *
from utils_scenario import *
from config import *
from utils import *
from de_auto_game import *
from utils_unitCounts import *

class MikeEmpires(DEAutoGame):

    # setup match data
    def setupData(self):

        self.matchData = getAllMatches()
        loadResults(self.matchData)
        self.all_combos = list(self.matchData.keys())
        self.combo_index = 0
        self.combo_offset = 0

    # check if hpPerDiff is statistically significant
    def checkConvergence(self, overdone_th=999):

        nameA = self.all_combos[self.combo_index]
        completed = True

        for _,(_,data) in self.matchData[nameA].items():

            fullCount = data["fullCount"]
            sterr = data["sterr"]
            stdev = data["stdev"]
            requiredMatches = pow(stdev/sterr_conv_threshold,2)

            # note: speculating that pending matches will complete
            if fullCount >= max_repeats: continue
            # note: but using non-speculated sterr here
            if fullCount >= min_repeats and sterr < sterr_conv_threshold: continue
            # note: below we speculate sterr convergence here
            if fullCount >= min_repeats and fullCount/requiredMatches >= overdone_th: continue

            completed = False
            break
        
        return completed

    # are all scenarios finished?
    def finished(self):

        num_combos = len(self.all_combos)
        if self.combo_index+self.combo_offset == num_combos-1 and self.checkConvergence():
            self.combo_index = num_combos
            self.combo_offset = 0
        if self.combo_index >= num_combos: 
            return True
        return False

    # add next xsdat into full dataset
    def processXSdata(self, scnData, xsdata):

        # add the xs data
        (c2, c3, a2, a3) = scnData
        addXSdata(c2, c3, a2, a3, xsdata, self.matchData)

    # setup next scenario
    def setupNextScenario(self):
        global matches_per_scenario, max_repeats, min_repeats, sterr_conv_threshold
                            
        # check if any combos remaining
        if self.finished():
            printd("there are no remaining scenarios")
            return (0,0,0,0)
        
        # check if convergence has been reached, if so then try next combo
        if self.checkConvergence(overdone_th=1.15): 
            printd("convergence has been reached")
            self.combo_index += 1
            return self.setupNextScenario()

        # if convergence will likely be reached, do the next combo before confirmed completion
        if self.combo_index < len(self.all_combos)-1 and self.checkConvergence(overdone_th=1.00): 
            printd("possible convergence has been reached")
            self.combo_index += 1
            self.combo_offset -= 1
            return self.setupNextScenario()

        # setup a new scenario
        f = ScenarioMatch()

        # get estimated remaining repeats for each combo
        nameA = self.all_combos[self.combo_index]
        print("index", self.combo_index)

        rcombo = []
        for nameB,(_,data) in self.matchData[nameA].items():

            # the number of completed + pending matches
            fullCount = data["fullCount"]
            stdev = data["stdev"]
            sterr = data["sterr"]
            count2 = data["completedCount"]

            repA = min_repeats - fullCount
            repB = max_repeats - fullCount
            repC = 1+1.10*pow(stdev/sterr_conv_threshold,2)-fullCount

            # todo: a little extra if unconverged so far

            repeats_left =  min(4*min_repeats,min(repB,max(repA, repC)))
            repeats_left = int(round(repeats_left))

            # if ACTUAL convergence has already been reach then prioritize other matches

            if (fullCount >= min_repeats and sterr < sterr_conv_threshold and count2 > 0) or fullCount >= max_repeats:
                repeats_left -= 14

            rcombo.append([repeats_left, nameB])

        # add all matches in combo until we hit the max
        printd("---- repeats-left ----")
        i = 0
        while True:

            # highest priority unit first; always prioritize not started matches
            rcombo = sorted(rcombo, key=lambda item: -item[0]-100 if self.matchData[nameA][item[1]][1]["fullCount"] == 0 else -item[0])

            # make sure there are some units avaliable
            maxRep = rcombo[0][0]
            if maxRep < 3:
                for r in rcombo: r[0] += 3-maxRep

            # loop over units in order of priority
            for j,(reps,nameB) in enumerate(rcombo):

                ((c2,c3,a2,a3,u2,u3),data) = self.matchData[nameA][nameB]
                if reps > 0:
                    print("- ", getUnit(u2), getUnit(u3), reps)

                closestRatio = getCounts(c2,c3,a2,a3,u2,u3,0.0)

                # decide how many units
                # n2 = int(num_units/2)
                # n3 = int(num_units/2)

                n2 = closestRatio[1]
                n3 = closestRatio[0]

                print("counts ", n2, n3)

                # create match for each repeat
                for k in range(reps):

                    # if too many units on map, then stop
                    # ...

                    # if too many matches, then stop
                    i += 1
                    if i > matches_per_scenario: break

                    f.createMatch(u2, u3, n2, n3, match_spacing, match_spacing)
                    self.matchData[nameA][nameB][1]["fullCount"] += 1
                    rcombo[j][0] -= 1

                # don't prioritize anything with unknown convergence
                if self.matchData[nameA][nameB][1]["completedCount"] == 0:
                    rcombo[j][0] -= 3

                if i > matches_per_scenario: break

            if i > matches_per_scenario: break

        # setup players
        f.setupPlayer(1, Civilization.FRANKS, StartingAge.POST_IMPERIAL_AGE)
        f.setupPlayer(2, c2, a2)
        f.setupPlayer(3, c3, a3)

        # write scenario file
        f.finish()

        self.combo_index += self.combo_offset
        self.combo_offset = 0

        # return known data
        scnData = (c2,c3,a2,a3)
        return scnData

    # save results to file
    def saveResults(self):
        saveResults(self.matchData)

    # print results
    def printResults(self):

        print("\n\n")
        print("hp percent delta [value, stdev, sterr, num-matches]")

        for _, dictt in self.matchData.items():
            for _, (info, data) in dictt.items():

                mean = float(100*data["mean"])
                stdev = float(100*data["stdev"])
                sterr = float(100*data["sterr"])
                count = data["completedCount"]

                (c2,c3,a2,a3,u2,u3) = info
                name  = ".".join((getCiv(c2),getAge(a2),getUnit(u2))) + " vs. "
                name += ".".join((getCiv(c3),getAge(a3),getUnit(u3)))

                print(name.rjust(20), "%.2f" % mean, "%.2f" % stdev, "%.2f" % sterr, count)

# -------------------------------

# create and run a new mike-empires
mike = MikeEmpires()
mike.setup()
mike.setupData()
mike.run()
mike.saveResults()
mike.printResults()

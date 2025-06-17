from AoE2ScenarioParser.datasets.object_support import *

from utils_unit_data import *
from utils_scenario import *
from config import *
from utils import *
from de_auto_game import *

class GetData(DEAutoGame):

    # setup match data
    def setupData(self):

        self.matchData = getAllMatches()
        loadResults(self.matchData)
        self.all_combos = list(self.matchData.keys())
        self.combo_index = -1

    # are all scenarios finished?
    def finished(self):

        if self.combo_index >= len(self.all_combos): 
            return True
        return False

    # add next xsdat into full dataset
    def processXSdata(self, scnData, xsdata):

        # add the xs data
        (c2,a2) = scnData
        addXSdata(c2, a2, xsdata, self.matchData)

    # setup next scenario
    def setupNextScenario(self):
        global matches_per_scenario, max_repeats, min_repeats, sterr_conv_threshold
                            
        self.combo_index += 1

        # check if any combos remaining
        if self.finished():
            printd("there are no remaining scenarios")
            return (None,None)
        
        # setup a new scenario
        f = ScenarioMatch(name="blankData.aoe2scenario")

        # get estimated remaining repeats for each combo
        nameA = self.all_combos[self.combo_index]

        # setup players
        unitz = list(self.matchData[nameA].keys())
        data = self.matchData[nameA][unitz[0]]
        c2 = data[0]
        a2 = data[1]
        
        f.setupPlayer(1, Civilization.FRANKS, StartingAge.POST_IMPERIAL_AGE)
        f.setupPlayer(2, c2, a2)
        f.setupPlayer(3, Civilization.FRANKS, StartingAge.POST_IMPERIAL_AGE)

        # write scenario file
        f.finish()


        # return known data
        scnData = (c2,a2)
        return scnData

    # save results to file
    def saveResults(self):
        saveResults(self.matchData)

    # print results
    def printResults(self):

        print("\n\n")
        print("hp percent delta [value, stdev, sterr, num-matches]")

        for _, dictt in self.matchData.items():
            for unit,data in dictt.items():

                cost = {}
                if data[3] > 0: cost["F"] = data[3]
                if data[4] > 0: cost["W"] = data[4]
                if data[5] > 0: cost["S"] = data[5]
                if data[6] > 0: cost["G"] = data[6]
                coststr = ", ".join([k+":"+str(v) for k,v in cost.items()])

                print(getCiv(data[0]), getAge(data[1]), getUnit(unit).ljust(15), coststr, data[7:])

# -------------------------------

# create and run a new mike-empires
mike = GetData()
mike.setup()
mike.setupData()
# mike.run()
mike.saveResults()
mike.printResults()

import pathlib
import numpy
from AoE2ScenarioParser.datasets.object_support import *
from AoE2ScenarioParser.datasets.units import *
from config import *
from utils_unitsList import *
from utils import *
import copy

# matchData format
# 
# {c2_a2:{u2i:(...), ..}}
# 
# ... = various stats
# .. = each unit
# 

# convert the match (civ, age) into unique name
def getMatchNameA(c2,a2):
    return "_".join((str(i) for i in (c2,a2)))

# get list of all possible matches based on the setup in config.py
def getAllMatches():

    matches = {}

    for c2 in civ_list:
        c2i = c2.value
        for a2 in age_list:
            a2i = a2.value
            nameA = getMatchNameA(c2i,a2i)
            matches[nameA] = {x.ID:(c2i,a2i,x.ID) for x in unitsList}

    return matches
            
# write results to file
def saveResults(matchData):

    data_folder = "data/"+game_version
    pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True)
    data_name = "unitData.csv"

    with open(data_folder+"/"+data_name, "w") as f:

        for _,dictt in matchData.items():
            for unit,data in dictt.items():
                for x in data[:-1]: f.write(str(x)+",")
                for x in data[-1:]: f.write(str(x)+"\n")
        
# load results from files
def loadResults(matchData):

    data_folder = "data/"+game_version
    pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True)

    # loop over all files in directory
    for filename in os.listdir(data_folder):
        if filename.endswith(".csv"):
            with open (os.path.join(data_folder, filename)) as f:
                lines = f.read().split("\n")
                for line in lines:
                    vals = line.split(",")
                    if len(vals) <= 1: continue
                    vals = [int(v) for v in vals]

                    c2 = vals[0]
                    a2 = vals[1]
                    u2 = vals[2]

                    nameA = getMatchNameA(c2,a2)
                    if not nameA in matchData: matchData[nameA] = { }
                    matchData[nameA][u2] = vals

# append xsdata into the matchData
def addXSdata(c2, a2, xsdat, matchData):

    # printd("process xs data")

    # process raw xs data into matches
    num_units = len(unitsList)
    if len(xsdat) % num_units != 0: raise Exception("invalid xsdat length")
    num_datas = int(len(xsdat) / num_units)
    for i in range(0,len(xsdat),num_datas):

        data = copy.deepcopy(xsdat[i:i+num_datas])
        data[0] = c2
        data[1] = a2

        # c2 = xsdat[i+0]
        # a2 = xsdat[i+1]
        u2 = xsdat[i+2]

        print("adding ", getCiv(c2), getAge(a2), getUnit(u2))

        nameA = getMatchNameA(c2,a2)
        if not u2 in matchData[nameA]: raise Exception("invalid unit")
        matchData[nameA][u2] = data

    print("added " + str("-".join((getCiv(c2), getAge(a2)))))

import pathlib
import numpy
from AoE2ScenarioParser.datasets.object_support import *
from AoE2ScenarioParser.datasets.units import *
from config import *

def lookupAge(age):
    if age == StartingAge.CASTLE_AGE:
        return "F"
    if age == StartingAge.IMPERIAL_AGE:
        return "C"
    if age == StartingAge.POST_IMPERIAL_AGE:
        return "I"
    return "D"

def getMatchName(a2_, a3_, c2_, c3_, u2_, u3_):

    a2 = lookupAge(a2_)
    a3 = lookupAge(a3_)
    c2 = c2_.name.lower().replace("_","-")
    c3 = c3_.name.lower().replace("_","-")
    u2 = UnitInfo.from_id(u2_).name.lower().replace("_","-")
    u3 = UnitInfo.from_id(u3_).name.lower().replace("_","-")

    name2 = a2 + "_" + c2 + "_" + u2
    name3 = a3 + "_" + c3 + "_" + u3
    name = name2 + " vs " + name3
    return name

# write results to file
def saveResults(matchData):

    data_folder = "data/"+game_version
    pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True)

    data_name = user_name + ".csv"
    counter = 0
    while pathlib.Path(data_folder+"/"+data_name).is_file():
        counter += 1
        data_name = user_name + "_" + str(counter) + ".csv"

    with open(data_folder+"/"+data_name, "w") as f:
        
        for name,mlist in matchData.items():

            for m in mlist:

                # loaded data
                f.write(str(m.unitId)+",")
                f.write(str(m.hpInitial)+",")
                f.write(str(m.hpFinal)+",")
                f.write(str(m.unitCount)+",")
                f.write(str(m.eunitId)+",")
                f.write(str(m.ehpInitial)+",")
                f.write(str(m.ehpFinal)+",")
                f.write(str(m.eunitCount)+",")
                f.write(str(m.status)+",")
                # constant data
                f.write(str(m.civ.value)+",")
                f.write(str(m.eciv.value)+",")
                f.write(str(m.age.value)+",")
                f.write(str(m.eage.value)+"\n")

def loadResults():

    data_folder = "data/"+game_version
    pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True)
    matchData = {}

    # loop over all files in directory
    for filename in os.listdir(data_folder):
        if filename.endswith(".csv"):
            with open (os.path.join(data_folder, filename)) as f:
                lines = f.read().split("\n")
                for line in lines:
                    
                    vals = line.split(",")
                    if len(vals) <= 1: continue
                    m = Match()
                    m.unitId = int(vals[0])
                    m.hpInitial = int(vals[1])
                    m.hpFinal = int(vals[2])
                    m.unitCount = int(vals[3])
                    m.eunitId = int(vals[4])
                    m.ehpInitial = int(vals[5])
                    m.ehpFinal = int(vals[6])
                    m.eunitCount = int(vals[7])
                    m.status = int(vals[8])
                    m.civ = Civilization(int(vals[9]))
                    m.eciv = Civilization(int(vals[10]))
                    m.age = StartingAge(int(vals[11]))
                    m.eage = StartingAge(int(vals[12]))

                    name = getMatchName(m.age, m.eage, m.civ, m.eciv, m.unitId, m.eunitId)
                    if name not in matchData:
                        matchData[name] = []
                    matchData[name].append(m)

    return matchData

def calculateStats(matchData):

    matchDataStats = {}

    # calculate stats for each matchup
    for name, mlist in matchData.items():

        hpPerDiff = []
        for m in mlist: hpPerDiff.append(m.hpFinal/m.hpInitial - m.ehpFinal/m.ehpInitial)
        mean = numpy.mean(hpPerDiff)
        std = numpy.std(hpPerDiff)
        count = len(hpPerDiff)
        sterr = std / numpy.sqrt(count)
        matchDataStats[name] = [mean, std, sterr, count]

    return matchDataStats

from AoE2ScenarioParser.datasets.object_support import *
from AoE2ScenarioParser.datasets.units import *
from config import *

def printd(val):
    if debug_print: print("DEBUG:",val)

def getCiv(val):
    return Civilization(val).name[:4].title()

def getUnit(val):
    return UnitInfo.from_id(val).name.title().replace("_","")

def getAge(val):
    val = StartingAge(val)
    if val == StartingAge.CASTLE_AGE: return "F"
    if val == StartingAge.IMPERIAL_AGE: return "C"
    if val == StartingAge.POST_IMPERIAL_AGE: return "I"
    return "D"

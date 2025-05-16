from AoE2ScenarioParser.datasets.object_support import *
from AoE2ScenarioParser.datasets.units import *

allUnits = {}

def addUnits(units):

    PF = []
    PC = []
    PI = []

    for (u,a) in units:

        if a <= 4: PI.append(u)
        if a <= 3: PC.append(u)
        if a <= 2: PF.append(u)

    return {StartingAge.CASTLE_AGE:PF, StartingAge.IMPERIAL_AGE:PC, StartingAge.POST_IMPERIAL_AGE:PI}


# armenians
tmp = [

[UnitInfo.ARCHER, 2],
[UnitInfo.SKIRMISHER, 2],
# [UnitInfo.SLINGER, 3],
[UnitInfo.CAVALRY_ARCHER, 3],
# [UnitInfo.ELEPHANT_ARCHER, 3],
# [UnitInfo.GENITOUR, 3],
# [UnitInfo.GRENADIER, 3],
# [UnitInfo.XIANBEI_RAIDER, 3],
# [UnitInfo.HAND_CANNONEER, 4],
[UnitInfo.MILITIA, 1],
[UnitInfo.SPEARMAN, 2], #---------
# [UnitInfo.EAGLE_SCOUT, 2],
# [UnitInfo.FIRE_LANCER, 3],
# [UnitInfo.JIAN_SWORDSMAN, 3],
# [UnitInfo.CONDOTTIERO, 4],
# [UnitInfo.FLEMISH_MILITIA, 2],
[UnitInfo.SCOUT_CAVALRY, 2],
# [UnitInfo.SHRIVAMSHA_RIDER, 3],
[UnitInfo.KNIGHT, 3],
# [UnitInfo.STEPPE_LANCER, 3],
# [UnitInfo.CAMEL_SCOUT, 3], #---------
# [UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3],
# [UnitInfo.XOLOTL_WARRIOR, 3],
[UnitInfo.MANGONEL, 3],
# [UnitInfo.ROCKET_CART, 3],
[UnitInfo.SCORPION, 3],
# [UnitInfo.BOMBARD_CANNON, 4],
# [UnitInfo.WAR_CHARIOT_FOCUS, 3],
[UnitInfo.COMPOSITE_BOWMAN, 3],
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# ----- ignored units -----
# [UnitInfo.BATTERING_RAM, 3], #--------- # OFF
# [UnitInfo.ARMORED_ELEPHANT, 3], # OFF
# [UnitInfo.FLAMING_CAMEL, 4], # OFF
# [UnitInfo.MOUNTED_TREBUCHET, 4], # OFF
# [UnitInfo.SIEGE_TOWER, 3], # OFF
# [UnitInfo.TRACTION_TREBUCHET, 4], # OFF
# [UnitInfo.PETARD, 3], # OFF
# [UnitInfo.TREBUCHET, 4], # OFF

]

allUnits[Civilization.ARMENIANS] = addUnits(tmp)


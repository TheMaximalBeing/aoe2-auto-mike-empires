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

# define units avaliable for each civ
# [<unit>, <age that unit is avaliable>]

# ARMENIANS
tmp = [

# --- archery-range ---
[UnitInfo.ARCHER, 2],
[UnitInfo.SKIRMISHER, 2],
# [UnitInfo.SLINGER, 3],
[UnitInfo.CAVALRY_ARCHER, 3],
# [UnitInfo.ELEPHANT_ARCHER, 3],
# [UnitInfo.GENITOUR, 3],
# [UnitInfo.GRENADIER, 3],
# [UnitInfo.XIANBEI_RAIDER, 3],
# [UnitInfo.HAND_CANNONEER, 4],
# --- barracks ---
[UnitInfo.MILITIA, 1],
[UnitInfo.SPEARMAN, 2],
# [UnitInfo.EAGLE_SCOUT, 2],
# [UnitInfo.FLEMISH_MILITIA, 2],
# [UnitInfo.FIRE_LANCER, 3],
# [UnitInfo.JIAN_SWORDSMAN, 3],
# [UnitInfo.CONDOTTIERO, 4],
# --- stable ---
[UnitInfo.SCOUT_CAVALRY, 2],
# [UnitInfo.SHRIVAMSHA_RIDER, 3],
[UnitInfo.KNIGHT, 3],
# [UnitInfo.STEPPE_LANCER, 3],
# [UnitInfo.CAMEL_SCOUT, 3],
# [UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3],
# [UnitInfo.XOLOTL_WARRIOR, 3],
# --- siege-workshop ---
[UnitInfo.BATTERING_RAM, 3],
# [UnitInfo.ARMORED_ELEPHANT, 3],
[UnitInfo.MANGONEL, 3],
# [UnitInfo.ROCKET_CART, 3],
[UnitInfo.SCORPION, 3],
[UnitInfo.SIEGE_TOWER, 3],
# [UnitInfo.WAR_CHARIOT_FOCUS, 3],
# [UnitInfo.BOMBARD_CANNON, 4],
# [UnitInfo.MOUNTED_TREBUCHET, 4],
# [UnitInfo.TRACTION_TREBUCHET, 4],
# [UnitInfo.FLAMING_CAMEL, 4],
# --- dock ---
[UnitInfo.FISHING_SHIP, 1],
[UnitInfo.TRANSPORT_SHIP, 1],
[UnitInfo.FIRE_GALLEY, 2],
[UnitInfo.TRADE_COG, 2],
[UnitInfo.DEMOLITION_RAFT, 2],
[UnitInfo.GALLEY, 2],
# [UnitInfo.TURTLE_SHIP, 3],
# [UnitInfo.LONGBOAT, 3],
# [UnitInfo.CARAVEL, 3],
[UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
# [UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.COMPOSITE_BOWMAN, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.ARMENIANS] = addUnits(tmp)

# add next civ here...


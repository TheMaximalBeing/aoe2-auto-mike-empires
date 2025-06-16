from AoE2ScenarioParser.datasets.object_support import *
from AoE2ScenarioParser.datasets.units import *

allUnits = {}

disabledUnits = [

# --- archery-range ---
# UnitInfo.ARCHER,
# UnitInfo.SKIRMISHER,
# UnitInfo.SLINGER,
# UnitInfo.CAVALRY_ARCHER,
# UnitInfo.ELEPHANT_ARCHER,
# UnitInfo.GENITOUR,
# UnitInfo.GRENADIER,
# UnitInfo.XIANBEI_RAIDER,
# UnitInfo.HAND_CANNONEER,
# --- barracks ---
# UnitInfo.MILITIA,
# UnitInfo.SPEARMAN,
# UnitInfo.EAGLE_SCOUT,
# UnitInfo.FLEMISH_MILITIA,
# UnitInfo.FIRE_LANCER,
# UnitInfo.JIAN_SWORDSMAN,
# UnitInfo.CONDOTTIERO,
# --- stable ---
# UnitInfo.SCOUT_CAVALRY,
# UnitInfo.SHRIVAMSHA_RIDER,
# UnitInfo.KNIGHT,
# UnitInfo.STEPPE_LANCER,
# UnitInfo.CAMEL_SCOUT,
# UnitInfo.BATTLE_ELEPHANT,
# UnitInfo.HEI_GUANG_CAVALRY,
# UnitInfo.XOLOTL_WARRIOR,
# --- siege-workshop ---
UnitInfo.BATTERING_RAM,
UnitInfo.ARMORED_ELEPHANT,
# UnitInfo.MANGONEL,
# UnitInfo.ROCKET_CART,
# UnitInfo.SCORPION,
UnitInfo.SIEGE_TOWER,
# UnitInfo.WAR_CHARIOT_FOCUS,
# UnitInfo.BOMBARD_CANNON,
# UnitInfo.MOUNTED_TREBUCHET, # !!!!!!
# UnitInfo.TRACTION_TREBUCHET, # !!!!!!
UnitInfo.FLAMING_CAMEL,
# --- dock ---
UnitInfo.FISHING_SHIP,
UnitInfo.TRANSPORT_SHIP,
UnitInfo.FIRE_GALLEY,
UnitInfo.TRADE_COG,
UnitInfo.DEMOLITION_RAFT,
UnitInfo.GALLEY, # !!!
UnitInfo.TURTLE_SHIP,
UnitInfo.LONGBOAT,
UnitInfo.CARAVEL,
UnitInfo.DROMON,
# UnitInfo.LOU_CHUAN,  # !!!!!!
UnitInfo.THIRISADAI,
UnitInfo.CANNON_GALLEON,
# --- monastery ---
# UnitInfo.MONK,
# UnitInfo.MISSIONARY,
# UnitInfo.WARRIOR_PRIEST,
# --- castle ---
# UnitInfo.COMPOSITE_BOWMAN,
UnitInfo.PETARD,
UnitInfo.TREBUCHET,

]

def addUnits(units):

    PF = []
    PC = []
    PI = []

    for (u,a) in units:

        if u in disabledUnits: continue

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
[UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.COMPOSITE_BOWMAN, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.ARMENIANS] = addUnits(tmp)

# AZTECS
tmp = [

# --- archery-range ---
[UnitInfo.ARCHER, 2],
[UnitInfo.SKIRMISHER, 2],
# [UnitInfo.SLINGER, 3],
# [UnitInfo.CAVALRY_ARCHER, 3],
# [UnitInfo.ELEPHANT_ARCHER, 3],
# [UnitInfo.GENITOUR, 3],
# [UnitInfo.GRENADIER, 3],
# [UnitInfo.XIANBEI_RAIDER, 3],
# [UnitInfo.HAND_CANNONEER, 4],
# --- barracks ---
[UnitInfo.MILITIA, 1],
[UnitInfo.SPEARMAN, 2],
[UnitInfo.EAGLE_SCOUT, 2],
# [UnitInfo.FLEMISH_MILITIA, 2],
# [UnitInfo.FIRE_LANCER, 3],
# [UnitInfo.JIAN_SWORDSMAN, 3],
# [UnitInfo.CONDOTTIERO, 4],
# --- stable ---
# [UnitInfo.SCOUT_CAVALRY, 2],
# [UnitInfo.SHRIVAMSHA_RIDER, 3],
# [UnitInfo.KNIGHT, 3],
# [UnitInfo.STEPPE_LANCER, 3],
# [UnitInfo.CAMEL_SCOUT, 3],
# [UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3],
[UnitInfo.XOLOTL_WARRIOR, 3],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
# [UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.JAGUAR_WARRIOR, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.AZTECS] = addUnits(tmp)

# BENGALIS
tmp = [

# --- archery-range ---
[UnitInfo.ARCHER, 2],
[UnitInfo.SKIRMISHER, 2],
# [UnitInfo.SLINGER, 3],
# [UnitInfo.CAVALRY_ARCHER, 3],
[UnitInfo.ELEPHANT_ARCHER, 3],
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
# [UnitInfo.KNIGHT, 3],
# [UnitInfo.STEPPE_LANCER, 3],
# [UnitInfo.CAMEL_SCOUT, 3],
[UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3],
# [UnitInfo.XOLOTL_WARRIOR, 3],
# --- siege-workshop ---
# [UnitInfo.BATTERING_RAM, 3],
[UnitInfo.ARMORED_ELEPHANT, 3],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.RATHA_MELEE, 3],
[UnitInfo.RATHA_RANGED, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.BENGALIS] = addUnits(tmp)

# BERBERS
tmp = [

# --- archery-range ---
[UnitInfo.ARCHER, 2],
[UnitInfo.SKIRMISHER, 2],
# [UnitInfo.SLINGER, 3],
[UnitInfo.CAVALRY_ARCHER, 3],
# [UnitInfo.ELEPHANT_ARCHER, 3],
[UnitInfo.GENITOUR, 3],
# [UnitInfo.GRENADIER, 3],
# [UnitInfo.XIANBEI_RAIDER, 3],
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.CAMEL_SCOUT, 3],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.CAMEL_ARCHER, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.BERBERS] = addUnits(tmp)

# BOHEMIANS
tmp = [

# --- archery-range ---
[UnitInfo.ARCHER, 2],
[UnitInfo.SKIRMISHER, 2],
# [UnitInfo.SLINGER, 3],
# [UnitInfo.CAVALRY_ARCHER, 3],
# [UnitInfo.ELEPHANT_ARCHER, 3],
# [UnitInfo.GENITOUR, 3],
# [UnitInfo.GRENADIER, 3],
# [UnitInfo.XIANBEI_RAIDER, 3],
[UnitInfo.HAND_CANNONEER, 3],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.HUSSITE_WAGON, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.BOHEMIANS] = addUnits(tmp)

# BRITONS
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.LONGBOWMAN, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.BRITONS] = addUnits(tmp)

# BULGARIANS
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.KONNIK, 3],
[UnitInfo.KONNIK_DISMOUNTED, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.BULGARIANS] = addUnits(tmp)

# BURGUNDIANS
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
[UnitInfo.HAND_CANNONEER, 4],
# --- barracks ---
[UnitInfo.MILITIA, 1],
[UnitInfo.SPEARMAN, 2],
# [UnitInfo.EAGLE_SCOUT, 2],
[UnitInfo.FLEMISH_MILITIA, 2],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.COUSTILLIER, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.BURGUNDIANS] = addUnits(tmp)

# BURMESE
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
[UnitInfo.BATTLE_ELEPHANT, 3],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.ARAMBAI, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.BURMESE] = addUnits(tmp)

# BYZANTINES
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
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.CAMEL_SCOUT, 3],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
[UnitInfo.CATAPHRACT, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.BYZANTINES] = addUnits(tmp)

# CELTS
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.WOAD_RAIDER, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.CELTS] = addUnits(tmp)

# CHINESE
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
# [UnitInfo.FIRE_LANCER, 3], # !!!!!!!!!!!!!!!!!! not working
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
# [UnitInfo.MANGONEL, 3],
# [UnitInfo.ROCKET_CART, 3], # !!!!!!!!!!!!!!!!!! not working
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4], # !!!!!!!!!!!!!!!!!! not working
# [UnitInfo.THIRISADAI, 4],
# [UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.CHU_KO_NU, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.CHINESE] = addUnits(tmp)

# CUMANS
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
[UnitInfo.STEPPE_LANCER, 3],
[UnitInfo.CAMEL_SCOUT, 3],
# [UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3],
# [UnitInfo.XOLOTL_WARRIOR, 3],
# --- siege-workshop ---
[UnitInfo.BATTERING_RAM, 2],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
# [UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.KIPCHAK, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.CUMANS] = addUnits(tmp)

# DRAVIDIANS
tmp = [

# --- archery-range ---
[UnitInfo.ARCHER, 2],
[UnitInfo.SKIRMISHER, 2],
# [UnitInfo.SLINGER, 3],
# [UnitInfo.CAVALRY_ARCHER, 3],
[UnitInfo.ELEPHANT_ARCHER, 3],
# [UnitInfo.GENITOUR, 3],
# [UnitInfo.GRENADIER, 3],
# [UnitInfo.XIANBEI_RAIDER, 3],
[UnitInfo.HAND_CANNONEER, 4],
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
# [UnitInfo.KNIGHT, 3],
# [UnitInfo.STEPPE_LANCER, 3],
# [UnitInfo.CAMEL_SCOUT, 3],
[UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3],
# [UnitInfo.XOLOTL_WARRIOR, 3],
# --- siege-workshop ---
# [UnitInfo.BATTERING_RAM, 3],
[UnitInfo.ARMORED_ELEPHANT, 3],
[UnitInfo.MANGONEL, 3],
# [UnitInfo.ROCKET_CART, 3],
[UnitInfo.SCORPION, 3],
[UnitInfo.SIEGE_TOWER, 3],
# [UnitInfo.WAR_CHARIOT_FOCUS, 3],
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
[UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.URUMI_SWORDSMAN, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.DRAVIDIANS] = addUnits(tmp)

# ETHIOPIANS
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
[UnitInfo.CAMEL_SCOUT, 3],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.SHOTEL_WARRIOR, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.ETHIOPIANS] = addUnits(tmp)

# FRANKS
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
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.THROWING_AXEMAN, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.FRANKS] = addUnits(tmp)

# GEORGIANS
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
[UnitInfo.HAND_CANNONEER, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.MONASPA, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.GEORGIANS] = addUnits(tmp)

# GOTHS
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
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
[UnitInfo.HUSKARL, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.GOTHS] = addUnits(tmp)

# GURJARAS
tmp = [

# --- archery-range ---
[UnitInfo.ARCHER, 2],
[UnitInfo.SKIRMISHER, 2],
# [UnitInfo.SLINGER, 3],
# [UnitInfo.CAVALRY_ARCHER, 3],
[UnitInfo.ELEPHANT_ARCHER, 3],
# [UnitInfo.GENITOUR, 3],
# [UnitInfo.GRENADIER, 3],
# [UnitInfo.XIANBEI_RAIDER, 3],
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.SHRIVAMSHA_RIDER, 3],
# [UnitInfo.KNIGHT, 3],
# [UnitInfo.STEPPE_LANCER, 3],
[UnitInfo.CAMEL_SCOUT, 3],
# [UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3],
# [UnitInfo.XOLOTL_WARRIOR, 3],
# --- siege-workshop ---
# [UnitInfo.BATTERING_RAM, 3],
[UnitInfo.ARMORED_ELEPHANT, 3],
[UnitInfo.MANGONEL, 3],
# [UnitInfo.ROCKET_CART, 3],
[UnitInfo.SCORPION, 3],
[UnitInfo.SIEGE_TOWER, 3],
# [UnitInfo.WAR_CHARIOT_FOCUS, 3],
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.CHAKRAM_THROWER, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.GURJARAS] = addUnits(tmp)

# HINDUSTANIS
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
[UnitInfo.HAND_CANNONEER, 4],
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
# [UnitInfo.KNIGHT, 3],
# [UnitInfo.STEPPE_LANCER, 3],
[UnitInfo.CAMEL_SCOUT, 2],
# [UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3],
# [UnitInfo.XOLOTL_WARRIOR, 3],
# --- siege-workshop ---
# [UnitInfo.BATTERING_RAM, 3],
[UnitInfo.ARMORED_ELEPHANT, 3],
[UnitInfo.MANGONEL, 3],
# [UnitInfo.ROCKET_CART, 3],
[UnitInfo.SCORPION, 3],
[UnitInfo.SIEGE_TOWER, 3],
# [UnitInfo.WAR_CHARIOT_FOCUS, 3],
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.GHULAM, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.HINDUSTANIS] = addUnits(tmp)

# HUNS
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
[UnitInfo.TARKAN, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.HUNS] = addUnits(tmp)

# INCAS
tmp = [

# --- archery-range ---
[UnitInfo.ARCHER, 2],
[UnitInfo.SKIRMISHER, 2],
[UnitInfo.SLINGER, 3],
# [UnitInfo.CAVALRY_ARCHER, 3],
# [UnitInfo.ELEPHANT_ARCHER, 3],
# [UnitInfo.GENITOUR, 3],
# [UnitInfo.GRENADIER, 3],
# [UnitInfo.XIANBEI_RAIDER, 3],
# [UnitInfo.HAND_CANNONEER, 4],
# --- barracks ---
[UnitInfo.MILITIA, 1],
[UnitInfo.SPEARMAN, 2],
[UnitInfo.EAGLE_SCOUT, 2],
# [UnitInfo.FLEMISH_MILITIA, 2],
# [UnitInfo.FIRE_LANCER, 3],
# [UnitInfo.JIAN_SWORDSMAN, 3],
# [UnitInfo.CONDOTTIERO, 4],
# --- stable ---
# [UnitInfo.SCOUT_CAVALRY, 2],
# [UnitInfo.SHRIVAMSHA_RIDER, 3],
# [UnitInfo.KNIGHT, 3],
# [UnitInfo.STEPPE_LANCER, 3],
# [UnitInfo.CAMEL_SCOUT, 3],
# [UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3],
[UnitInfo.XOLOTL_WARRIOR, 3],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
# [UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.KAMAYUK, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.INCAS] = addUnits(tmp)

# ITALIANS
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
[UnitInfo.HAND_CANNONEER, 4],
# --- barracks ---
[UnitInfo.MILITIA, 1],
[UnitInfo.SPEARMAN, 2],
# [UnitInfo.EAGLE_SCOUT, 2],
# [UnitInfo.FLEMISH_MILITIA, 2],
# [UnitInfo.FIRE_LANCER, 3],
# [UnitInfo.JIAN_SWORDSMAN, 3],
[UnitInfo.CONDOTTIERO, 4],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.GENOESE_CROSSBOWMAN, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.ITALIANS] = addUnits(tmp)

# JAPANESE
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
[UnitInfo.HAND_CANNONEER, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.SAMURAI, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.JAPANESE] = addUnits(tmp)

# JURCHENS
tmp = [

# --- archery-range ---
[UnitInfo.ARCHER, 2],
[UnitInfo.SKIRMISHER, 2],
# [UnitInfo.SLINGER, 3],
[UnitInfo.CAVALRY_ARCHER, 3],
# [UnitInfo.ELEPHANT_ARCHER, 3],
# [UnitInfo.GENITOUR, 3],
# [UnitInfo.GRENADIER, 3], # !!!!!!!!!!!!!!!!!! not working
# [UnitInfo.XIANBEI_RAIDER, 3],
# [UnitInfo.HAND_CANNONEER, 4],
# --- barracks ---
[UnitInfo.MILITIA, 1],
[UnitInfo.SPEARMAN, 2],
# [UnitInfo.EAGLE_SCOUT, 2],
# [UnitInfo.FLEMISH_MILITIA, 2],
# [UnitInfo.FIRE_LANCER, 3], # !!!!!!!!!!!!!!!!!! not working
# [UnitInfo.JIAN_SWORDSMAN, 3],
# [UnitInfo.CONDOTTIERO, 4],
# --- stable ---
[UnitInfo.SCOUT_CAVALRY, 2],
# [UnitInfo.SHRIVAMSHA_RIDER, 3],
# [UnitInfo.KNIGHT, 3],
[UnitInfo.STEPPE_LANCER, 3],
# [UnitInfo.CAMEL_SCOUT, 3],
# [UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3],
# [UnitInfo.XOLOTL_WARRIOR, 3],
# --- siege-workshop ---
[UnitInfo.BATTERING_RAM, 3],
# [UnitInfo.ARMORED_ELEPHANT, 3],
# [UnitInfo.MANGONEL, 3],
# [UnitInfo.ROCKET_CART, 3], # !!!!!!!!!!!!!!!!!! not working
[UnitInfo.SCORPION, 3],
[UnitInfo.SIEGE_TOWER, 3],
# [UnitInfo.WAR_CHARIOT_FOCUS, 3],
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4], # !!!!!!!!!!!!!!!!!! not working
# [UnitInfo.THIRISADAI, 4],
# [UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
# [UnitInfo.IRON_PAGODA, 3], # !!!!!!!!!!!!!!!!!! not working
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.JURCHENS] = addUnits(tmp)

# KHITANS
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
# [UnitInfo.FIRE_LANCER, 3], # !!!!!!!!!!!!!!!!!! not working
# [UnitInfo.JIAN_SWORDSMAN, 3],
# [UnitInfo.CONDOTTIERO, 4],
# --- stable ---
[UnitInfo.SCOUT_CAVALRY, 2],
# [UnitInfo.SHRIVAMSHA_RIDER, 3],
# [UnitInfo.KNIGHT, 3],
[UnitInfo.STEPPE_LANCER, 3],
[UnitInfo.CAMEL_SCOUT, 3],
# [UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3],
# [UnitInfo.XOLOTL_WARRIOR, 3],
# --- siege-workshop ---
[UnitInfo.BATTERING_RAM, 3],
# [UnitInfo.ARMORED_ELEPHANT, 3],
# [UnitInfo.MANGONEL, 3],
# [UnitInfo.ROCKET_CART, 3], # !!!!!!!!!!!!!!!!!! not working
[UnitInfo.SCORPION, 3],
[UnitInfo.SIEGE_TOWER, 3],
# [UnitInfo.WAR_CHARIOT_FOCUS, 3],
# [UnitInfo.BOMBARD_CANNON, 4],
# [UnitInfo.MOUNTED_TREBUCHET, 4], # !!!!!!!!!!!!!!!!!! not working
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
# [UnitInfo.LIAO_DAO, 3], # !!!!!!!!!!!!!!!!!! not working
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.KHITANS] = addUnits(tmp)

# KHMER
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
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.BATTLE_ELEPHANT, 3],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.BALLISTA_ELEPHANT, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.KHMER] = addUnits(tmp)

# KOREANS
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
[UnitInfo.HAND_CANNONEER, 4],
# --- barracks ---
[UnitInfo.MILITIA, 1],
[UnitInfo.SPEARMAN, 2],
# [UnitInfo.EAGLE_SCOUT, 2],
# [UnitInfo.FLEMISH_MILITIA, 2],
# [UnitInfo.FIRE_LANCER, 3], # !!!!!!!!!!!!!!!!!! not working
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
# [UnitInfo.MANGONEL, 3],
# [UnitInfo.ROCKET_CART, 3], # !!!!!!!!!!!!!!!!!! not working
[UnitInfo.SCORPION, 3],
[UnitInfo.SIEGE_TOWER, 3],
# [UnitInfo.WAR_CHARIOT_FOCUS, 3],
[UnitInfo.BOMBARD_CANNON, 4],
# [UnitInfo.MOUNTED_TREBUCHET, 4],
# [UnitInfo.TRACTION_TREBUCHET, 4],
# [UnitInfo.FLAMING_CAMEL, 4],
# --- dock ---
[UnitInfo.FISHING_SHIP, 1],
[UnitInfo.TRANSPORT_SHIP, 1],
[UnitInfo.FIRE_GALLEY, 2],
[UnitInfo.TRADE_COG, 2],
# [UnitInfo.DEMOLITION_RAFT, 2],
[UnitInfo.GALLEY, 2],
[UnitInfo.TURTLE_SHIP, 3],
# [UnitInfo.LONGBOAT, 3],
# [UnitInfo.CARAVEL, 3],
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.WAR_WAGON, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.KOREANS] = addUnits(tmp)

# LITHUANIANS
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
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.WINGED_HUSSAR, 4],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.LEITIS, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.LITHUANIANS] = addUnits(tmp)

# MAGYARS
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.MAGYAR_HUSZAR, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.MAGYARS] = addUnits(tmp)

# MALAY
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
[UnitInfo.BATTLE_ELEPHANT, 3],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.KARAMBIT_WARRIOR, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.MALAY] = addUnits(tmp)

# MALIANS
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
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.CAMEL_SCOUT, 3],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.GBETO, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.MALIANS] = addUnits(tmp)

# MAYANS
tmp = [

# --- archery-range ---
[UnitInfo.ARCHER, 2],
[UnitInfo.SKIRMISHER, 2],
# [UnitInfo.SLINGER, 3],
# [UnitInfo.CAVALRY_ARCHER, 3],
# [UnitInfo.ELEPHANT_ARCHER, 3],
# [UnitInfo.GENITOUR, 3],
# [UnitInfo.GRENADIER, 3],
# [UnitInfo.XIANBEI_RAIDER, 3],
# [UnitInfo.HAND_CANNONEER, 4],
# --- barracks ---
[UnitInfo.MILITIA, 1],
[UnitInfo.SPEARMAN, 2],
[UnitInfo.EAGLE_SCOUT, 2],
# [UnitInfo.FLEMISH_MILITIA, 2],
# [UnitInfo.FIRE_LANCER, 3],
# [UnitInfo.JIAN_SWORDSMAN, 3],
# [UnitInfo.CONDOTTIERO, 4],
# --- stable ---
# [UnitInfo.SCOUT_CAVALRY, 2],
# [UnitInfo.SHRIVAMSHA_RIDER, 3],
# [UnitInfo.KNIGHT, 3],
# [UnitInfo.STEPPE_LANCER, 3],
# [UnitInfo.CAMEL_SCOUT, 3],
# [UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3],
[UnitInfo.XOLOTL_WARRIOR, 3],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
# [UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.PLUMED_ARCHER, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.MAYANS] = addUnits(tmp)

# MONGOLS
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
[UnitInfo.STEPPE_LANCER, 3],
[UnitInfo.CAMEL_SCOUT, 3],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.MANGUDAI, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.MONGOLS] = addUnits(tmp)

# PERSIANS
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
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.CAMEL_SCOUT, 3],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.WAR_ELEPHANT, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.PERSIANS] = addUnits(tmp)

# POLES
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
[UnitInfo.WINGED_HUSSAR, 4],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.OBUCH, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.POLES] = addUnits(tmp)

# PORTUGUESE
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
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
[UnitInfo.CARAVEL, 3],
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.ORGAN_GUN, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.PORTUGUESE] = addUnits(tmp)

# ROMANS
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
# [UnitInfo.DEMOLITION_RAFT, 2],
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
[UnitInfo.CENTURION, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.ROMANS] = addUnits(tmp)

# SARACENS
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
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.CAMEL_SCOUT, 3],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.MAMELUKE, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.SARACENS] = addUnits(tmp)

# SHU
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
# [UnitInfo.KNIGHT, 3],
# [UnitInfo.STEPPE_LANCER, 3],
# [UnitInfo.CAMEL_SCOUT, 3],
# [UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3], # !!!!!!!!!!!!!!!!!! not working
# [UnitInfo.XOLOTL_WARRIOR, 3],
# --- siege-workshop ---
[UnitInfo.BATTERING_RAM, 3],
# [UnitInfo.ARMORED_ELEPHANT, 3],
[UnitInfo.MANGONEL, 3],
# [UnitInfo.ROCKET_CART, 3],
# [UnitInfo.SCORPION, 3],
[UnitInfo.SIEGE_TOWER, 3],
# [UnitInfo.WAR_CHARIOT_FOCUS, 3], # !!!!!!!!!!!!!!!!!! not working
# [UnitInfo.BOMBARD_CANNON, 4],
# [UnitInfo.MOUNTED_TREBUCHET, 4],
# [UnitInfo.TRACTION_TREBUCHET, 4], # !!!!!!!!!!!!!!!!!! not working
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4], # !!!!!!!!!!!!!!!!!! not working
# [UnitInfo.THIRISADAI, 4],
# [UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
# [UnitInfo.WHITE_FEATHER_GUARD, 3], # !!!!!!!!!!!!!!!!!! not working
[UnitInfo.PETARD, 3],
# [UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.SHU] = addUnits(tmp)

# SICILIANS
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.SERJEANT, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.SICILIANS] = addUnits(tmp)

# SLAVS
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.BOYAR, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.SLAVS] = addUnits(tmp)

# SPANISH
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
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
[UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.CONQUISTADOR, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.SPANISH] = addUnits(tmp)

# TATARS
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
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.STEPPE_LANCER, 3],
[UnitInfo.CAMEL_SCOUT, 3],
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
[UnitInfo.FLAMING_CAMEL, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.KESHIK, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.TATARS] = addUnits(tmp)

# TEUTONS
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
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.TEUTONIC_KNIGHT, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.TEUTONS] = addUnits(tmp)

# TURKS
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
[UnitInfo.HAND_CANNONEER, 4],
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
[UnitInfo.CAMEL_SCOUT, 3],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.JANISSARY, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.TURKS] = addUnits(tmp)

# VIETNAMESE
tmp = [

# --- archery-range ---
[UnitInfo.ARCHER, 2],
[UnitInfo.SKIRMISHER, 2],
[UnitInfo.IMPERIAL_SKIRMISHER, 4],
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
# [UnitInfo.FIRE_LANCER, 3], # !!!!!!!!!!!!!!!!!! not working
# [UnitInfo.JIAN_SWORDSMAN, 3],
# [UnitInfo.CONDOTTIERO, 4],
# --- stable ---
[UnitInfo.SCOUT_CAVALRY, 2],
# [UnitInfo.SHRIVAMSHA_RIDER, 3],
[UnitInfo.KNIGHT, 3],
# [UnitInfo.STEPPE_LANCER, 3],
# [UnitInfo.CAMEL_SCOUT, 3],
[UnitInfo.BATTLE_ELEPHANT, 3],
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
[UnitInfo.BOMBARD_CANNON, 4],
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.RATTAN_ARCHER, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.VIETNAMESE] = addUnits(tmp)

# VIKINGS
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
# [UnitInfo.FIRE_GALLEY, 2],
[UnitInfo.TRADE_COG, 2],
[UnitInfo.DEMOLITION_RAFT, 2],
[UnitInfo.GALLEY, 2],
# [UnitInfo.TURTLE_SHIP, 3],
[UnitInfo.LONGBOAT, 3],
# [UnitInfo.CARAVEL, 3],
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4],
# [UnitInfo.THIRISADAI, 4],
[UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
[UnitInfo.BERSERK, 3],
[UnitInfo.PETARD, 3],
[UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.VIKINGS] = addUnits(tmp)

# WEI
tmp = [

# --- archery-range ---
[UnitInfo.ARCHER, 2],
[UnitInfo.SKIRMISHER, 2],
# [UnitInfo.SLINGER, 3],
# [UnitInfo.CAVALRY_ARCHER, 3],
# [UnitInfo.ELEPHANT_ARCHER, 3],
# [UnitInfo.GENITOUR, 3],
# [UnitInfo.GRENADIER, 3],
# [UnitInfo.XIANBEI_RAIDER, 3], # !!!!!!!!!!!!!!!!!! not working
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
# [UnitInfo.KNIGHT, 3],
# [UnitInfo.STEPPE_LANCER, 3],
# [UnitInfo.CAMEL_SCOUT, 3],
# [UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3], # !!!!!!!!!!!!!!!!!! not working
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
# [UnitInfo.TRACTION_TREBUCHET, 4], # !!!!!!!!!!!!!!!!!! not working
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4], # !!!!!!!!!!!!!!!!!! not working
# [UnitInfo.THIRISADAI, 4],
# [UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
# [UnitInfo.TIGER_CAVALRY, 3], # !!!!!!!!!!!!!!!!!! not working
[UnitInfo.PETARD, 3],
# [UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.WEI] = addUnits(tmp)

# WU
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
# [UnitInfo.JIAN_SWORDSMAN, 3], # !!!!!!!!!!!!!!!!!! not working
# [UnitInfo.CONDOTTIERO, 4],
# --- stable ---
[UnitInfo.SCOUT_CAVALRY, 2],
# [UnitInfo.SHRIVAMSHA_RIDER, 3],
# [UnitInfo.KNIGHT, 3],
# [UnitInfo.STEPPE_LANCER, 3],
# [UnitInfo.CAMEL_SCOUT, 3],
# [UnitInfo.BATTLE_ELEPHANT, 3],
# [UnitInfo.HEI_GUANG_CAVALRY, 3], # !!!!!!!!!!!!!!!!!! not working
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
# [UnitInfo.TRACTION_TREBUCHET, 4], # !!!!!!!!!!!!!!!!!! not working
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
# [UnitInfo.DROMON, 4],
# [UnitInfo.LOU_CHUAN, 4], # !!!!!!!!!!!!!!!!!! not working
# [UnitInfo.THIRISADAI, 4],
# [UnitInfo.CANNON_GALLEON, 4],
# --- monastery ---
[UnitInfo.MONK, 3],
# [UnitInfo.MISSIONARY, 3],
# [UnitInfo.WARRIOR_PRIEST, 3],
# --- castle ---
# [UnitInfo.FIRE_ARCHER, 3], # !!!!!!!!!!!!!!!!!! not working
[UnitInfo.PETARD, 3],
# [UnitInfo.TREBUCHET, 4],

]

allUnits[Civilization.WU] = addUnits(tmp)

# add next civ here...


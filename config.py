
from AoE2ScenarioParser.datasets.object_support import *
import os

# game version
game_version = "101.103.13286.0"

# name of AutoMatch user
user_name = "TMB"

# benchmark score of user
user_benchmark = 1000

# location of xs data folder
folder_xsdat = "%USERPROFILE%/Games/Age of Empires 2 DE/76561198273299929/profile"

# location of scenario folder
folder_scn = "%USERPROFILE%/Games/Age of Empires 2 DE/76561198273299929/resources/_common/scenario"

# name of xs data file
name_xs_data = "PromiDE.xsdat" # always writes to PromiDE due to bug

# name of base scenario file
name_scn_base = "blank.aoe2scenario"

# name of modified scenario file
name_scn_mod = "output.aoe2scenario"

# debug prints enabled
debug_print = True

# maximum number of matches per scenario
matches_per_scenario = 60

# minimum number of times a specific match should be repreated
min_repeats = 6

# maximum number of times a specific match should be repreated
max_repeats = 24

# maximum number of the same type of match per scenario
max_per_scenario = 18

# goal for standard error; we repeat matches until it falls below this value
sterr_conv_threshold = 0.04

# list of all civs considered for automatch
# civ_list = [ 
#     Civilization.ARMENIANS, Civilization.AZTECS, Civilization.BENGALIS, Civilization.BERBERS, Civilization.BOHEMIANS, 
#     Civilization.BRITONS, Civilization.BULGARIANS, Civilization.BURGUNDIANS, Civilization.BURMESE, Civilization.BYZANTINES, 
#     Civilization.CELTS, Civilization.CHINESE, Civilization.CUMANS, Civilization.DRAVIDIANS 
# ]

civ_list = [ 
    Civilization.BYZANTINES
]

# list of all ages considered for automatch (N.B. units are actually from the previous age)
age_list = [ StartingAge.POST_IMPERIAL_AGE]#, StartingAge.IMPERIAL_AGE, StartingAge.POST_IMPERIAL_AGE ]

# ideal number of units per group; may be changed to balance resources
num_units = 20

# maximum difference allowed from ideal number of units
num_units_delta = 2

# "fixed_number" or "total_resources"
type = "fixed_number"

# how much each resource is worth
resource_weights = { 
    
    "F":{"F":1.40, "W":0.90, "S":1.00, "G":1.00},
    "C":{"F":1.20, "W":1.00, "S":1.00, "G":1.00},
    # "I":{"F":1.00, "W":1.00, "S":1.00, "G":1.20},
    "I":{"F":1.00, "W":1.00, "S":1.00, "G":3.50}, # no gold version
}

# spacing between matches; must be same as autoMatch.hpp
match_spacing = 24

# data for each match; must be same as autoMatch.hpp
class Match:
    # loaded data
    unitId = 0
    hpInitial = 0
    hpFinal = 0
    unitCount = 0
    eunitId = 0
    ehpInitial = 0
    ehpFinal = 0
    eunitCount = 0
    status = 0
    # microType = 0
    # emicroType = 0
    
    # constant data
    civ = 0
    eciv = 0
    age = 0
    eage = 0

# number of goals that are loaded per match; mudt be consistent with above struct
sizeMatch = 9

# resolve %USERPROFILE% in paths
folder_xsdat = os.path.expandvars(folder_xsdat)
folder_scn = os.path.expandvars(folder_scn)

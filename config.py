
from AoE2ScenarioParser.datasets.object_support import *
import os

# name of AutoMatch user
user_name = "TMB"

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
max_repeats = 120

# goal for standard error; we repeat matches until it falls below this value
sterr_conv_threshold = 0.02

# list of all civs considered for automatch
civ_list = [ Civilization.ARMENIANS ]

# list of all ages considered for automatch (N.B. units are actually from the pervious age)
age_list = [ StartingAge.CASTLE_AGE]#, StartingAge.IMPERIAL_AGE, StartingAge.POST_IMPERIAL_AGE ]

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

# number of goals that are loaded per match
sizeMatch = 9

# resolve %USERPROFILE% in paths
folder_xsdat = os.path.expandvars(folder_xsdat)
folder_scn = os.path.expandvars(folder_scn)

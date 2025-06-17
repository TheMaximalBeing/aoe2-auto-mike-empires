from AoE2ScenarioParser.datasets.players import *
from AoE2ScenarioParser.datasets.units import *
from AoE2ScenarioParser.datasets.buildings import *
from AoE2ScenarioParser.datasets.techs import *
from AoE2ScenarioParser.datasets.terrains import *
from AoE2ScenarioParser.datasets.object_support import *
from AoE2ScenarioParser.datasets.other import *
from AoE2ScenarioParser.datasets.trigger_lists.diplomacy_state import *
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import *
from AoE2ScenarioParser import settings
import math
from config import *

settings.PRINT_STATUS_UPDATES = False

def _getPositions(count):
    pos = []
    rows = math.ceil(math.sqrt(count))
    x = 0
    y = 0
    for i in range(count):
        pos.append((x,y))
        x += 1
        if x >= rows:
            x = 0
            y += 1
    return pos

counter = 0

class ScenarioMatch:

    def __init__(self):
        self.scenario = AoE2DEScenario.from_file(folder_scn + "/" + name_scn_base)
        self.trigger_manager = self.scenario.trigger_manager
        self.unit_manager = self.scenario.unit_manager
        self.map_manager = self.scenario.map_manager
        self.player_manager = self.scenario.player_manager
        self.option_manager = self.scenario.option_manager

        self.player_manager.active_players = 3

        for i in range(8):
            p = self.player_manager.players[i]
            # p.human = False
            p.food = 500
            p.wood = 500
            p.stone = 500
            p.gold = 500

        # map_manager.map_size = 480
        self.map_size = self.map_manager.map_size
        self.match_x = 0
        self.match_y = 0

    def finish(self):
        self.unit_manager.add_unit(player=1, unit_const=UnitInfo.SPEARMAN.ID, x=self.map_size-1,y=self.map_size-1)
        self.scenario.write_to_file(folder_scn + "/" + name_scn_mod)

    def setupPlayer(self, player, civ, age):
        self.player_manager.players[player].civilization = civ
        self.player_manager.players[player].architecture_set = civ
        self.player_manager.players[player].starting_age = age

    def createMatch(self, unitA, unitB, countA, countB, size, spacing):

        lerp = size+spacing
        if self.match_x+lerp >= self.map_size:
            self.match_x = 0
            self.match_y += lerp
        if self.match_y+lerp >= self.map_size:
            raise Exception("scenario doesn't have enough space for the next match")

        for x in range(self.match_x, self.match_x+lerp):
            for y in range(self.match_y, self.match_y+lerp):
                if x < self.match_x+size and y < self.match_y+size:
                    continue
                tile = self.map_manager.get_tile(x, y)
                tile.terrain_id = TerrainId.WATER_DEEP_OCEAN

        global counter

        for p in _getPositions(countA):
            if counter % 2 == 0:
                self.unit_manager.add_unit(player=2, unit_const=unitA, x=p[0]+self.match_x, y=p[1]+self.match_y)
            else: 
                self.unit_manager.add_unit(player=2, unit_const=unitA, x=size-p[0]-1+self.match_x, y=size-p[1]-1+self.match_y)
        
        for p in _getPositions(countB):
            if counter % 2 == 0:
                self.unit_manager.add_unit(player=3, unit_const=unitB, x=size-p[0]-1+self.match_x, y=size-p[1]-1+self.match_y)
            else:
                self.unit_manager.add_unit(player=3, unit_const=unitB, x=p[0]+self.match_x, y=p[1]+self.match_y)

        self.match_x+=lerp
        counter += 1

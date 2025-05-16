# aoe2-auto-mike-empires
### *A tool for automating unit vs. unit matches in Age of Empires II: Definitive Edition*

## Dependencies

- a python interpreter
- pip install AoE2ScenarioParser 
- pip install pynput
- pip install pygetwindow
- pip install numpy

## Installation

- copy **Dump.xs** to **.../steamapps/common/AoE2DE/resources/_common/xs**
- copy **AutoMatch.per** and **AutoMatch.ai** to **.../steamapps/common/AoE2DE/resources/_common/ai**
- copy **blank.aoe2scenario** and **output.aoe2scenario** to **%USERPROFILE%/Games/Age of Empires 2 DE/*number*/resources/_common/scenario**
- open **config.py** and set the values for *user_name*, *folder_xsdat*, *folder_scn*; ensure the correct profile number is used

## How to use

- launch game and start the **output** scenario from the skirmish menu
- set the hotkey for *Menu* to *F10*
- run **run_matches.py**; this will generate and run the **output** scenario
- leave the mouse towards the side of the game window
- wait until **run_matches.py** reports that all matches are complete
- do not move the mouse until everything is done[^1]
- do not change the focus window until everything is done[^1]

---

[^1]: **run_matches.py** will input keyboard presses to restart the game automatically. This will fail if the mouse is hovering over the menu or is being moved while a restart is attempted. If the restart fails then you will need to manually restart the game.

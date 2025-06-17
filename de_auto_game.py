import os
import time
import pynput.keyboard
import pygetwindow

from utils import *
from config import *


class DEAutoGame():

    # setup game
    def setup(self):

        # focus on AoEII window so that keystrokes work
        printd("switch to AoE II window")
        target_windows = pygetwindow.getWindowsWithTitle("Age of Empires II:")
        if target_windows: target_window = target_windows[0]
        else: raise Exception("Could not find Age of Empires window")
        target_window.activate()

        # setup for xsdat
        self.xsdatfile = folder_xsdat + "/" + name_xs_data
        self.moddate = time.ctime(os.stat(self.xsdatfile)[8]) # last modified time
        self.keyboard = pynput.keyboard.Controller()

    # override me
    # have we completed all scenarios
    def finished(self):
        return False

    # restart scenario
    def restartScenario(self):
        
        global moddate
        printd("restart match")
        # target_window.activate()
        # time.sleep(0.2)
        # self.keyboard.tap(pynput.keyboard.Key.esc)
        # time.sleep(0.3)
        # self.keyboard.tap(pynput.keyboard.Key.f10)
        # time.sleep(1.5)
        # for i in range(6):
        #     self.keyboard.tap(pynput.keyboard.Key.tab)
        #     time.sleep(0.2)
        # self.keyboard.tap(pynput.keyboard.Key.enter)
        # time.sleep(0.8)
        # self.keyboard.tap(pynput.keyboard.Key.tab)
        # time.sleep(0.2)
        # self.keyboard.tap(pynput.keyboard.Key.enter)
        # time.sleep(0.2)
        # self.keyboard.tap(pynput.keyboard.Key.esc)

        # game menu
        time.sleep(0.2)
        self.keyboard.tap(pynput.keyboard.Key.esc)
        time.sleep(0.3)
        self.keyboard.tap(pynput.keyboard.Key.f10)
        time.sleep(1.5)
        self.keyboard.tap(pynput.keyboard.Key.tab)
        self.keyboard.tap(pynput.keyboard.Key.enter)

        # are you sure
        time.sleep(0.8)
        self.keyboard.tap(pynput.keyboard.Key.tab)
        time.sleep(0.2)
        self.keyboard.tap(pynput.keyboard.Key.enter)
        time.sleep(0.2)
        self.keyboard.tap(pynput.keyboard.Key.tab)
        time.sleep(0.2)
        self.keyboard.tap(pynput.keyboard.Key.enter)
        time.sleep(1.0)

        # game stats
        time.sleep(0.2)
        self.keyboard.tap(pynput.keyboard.Key.esc)

        # single player
        time.sleep(1.5)
        self.keyboard.tap(pynput.keyboard.Key.tab)
        time.sleep(0.2)
        self.keyboard.tap(pynput.keyboard.Key.tab)
        time.sleep(0.2)
        self.keyboard.tap(pynput.keyboard.Key.tab)
        time.sleep(0.2)
        self.keyboard.tap(pynput.keyboard.Key.enter)

        # skirmish
        time.sleep(0.2)
        self.keyboard.tap(pynput.keyboard.Key.tab)
        time.sleep(0.2)
        self.keyboard.tap(pynput.keyboard.Key.tab)
        time.sleep(0.2)
        self.keyboard.tap(pynput.keyboard.Key.enter)

        # start game
        time.sleep(1.5)
        for i in range(9):
            self.keyboard.tap(pynput.keyboard.Key.tab)
            time.sleep(0.2)
        self.keyboard.tap(pynput.keyboard.Key.enter)

        # time.sleep(0.2)
        # self.keyboard.tap(pynput.keyboard.Key.esc)

        # clear xs data file and reset moddate
        printd("clear xsdat file")
        with open(self.xsdatfile, "wb") as f: pass # clear file
        moddate = time.ctime(os.stat(self.xsdatfile)[8])

        # wait enough time for the game to restart
        printd("waiting for game to restart")
        time.sleep(8)

    # override me
    # process the xs data
    def processXSdata(self, scnData, xsdata):
        pass

    # override me
    def setupNextScenario(seld):
        pass

    # run the scenarios until everything is finished
    def run(self):

        # setup the first scenario
        scnData_ = self.setupNextScenario()

        # loop over all scenarios
        while True:

            # check if there are any matches remaining
            if self.finished():
                print("all matches have been completed")
                break

            # run next scenario and collect constants
            print("running next set of matches")
            self.restartScenario()
            scnData = scnData_
            scnData_ = self.setupNextScenario()

            # wait until file has been modified
            printd("waiting for xsdata modify")
            while True:
                moddate2 = time.ctime(os.stat(self.xsdatfile)[8])
                if moddate2 > moddate: break
                time.sleep(0.3)
            time.sleep(1.5) # allow more time for file to be written

            # extract all data from xsdat
            printd("extracting data from xsdat")
            xsdata = []
            with open(self.xsdatfile, "rb") as f:
                contents = f.read()
                size = len(contents)
                if size == 0: raise Exception("empty xs data file")
                if size % 4 != 0: raise Exception("xs data file size is not a multiple of 4")
                for i in range(0,size,4):
                    xsdata.append(int.from_bytes(contents[i:i+4],byteorder="little", signed=True))
        
            # add the xs data
            self.processXSdata(scnData, xsdata)

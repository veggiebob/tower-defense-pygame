import pygame, sys
from game.subsystems.environment import *
from pygame.locals import *
pygame.init()

class Testing ():
    def __init__(self):
        self.test = Environment()

    def pathTest(self):
        testingString = ""
        for i in range(0, len(self.test.board[0]), 1):
            testingString = ""
            for j in range(0, len(self.test.board), 1):
                if self.test.board[j][i].getPath():
                    testingString += " P"
                else:
                    testingString += " N"
            print(testingString)

        added = False
        for i in range(0, len(self.test.board[0]), 1):
            testingString = ""
            for j in range(0, len(self.test.board), 1):
                for k in range(0, self.test.pathes[0].pathLength() - 1, 0):
                    tempPoint = self.test.pathes[0].returnPoint(k)
                    if tempPoint.getX() == i and tempPoint.getY() == j:
                        testingString += " P"
                        added = True
                if not added:
                    testingString += " N"

        def timeTest(self):
            randInt = 2

envirTest = Testing()

envirTest.pathTest()


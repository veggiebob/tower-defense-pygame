import pygame, sys
from game.subsystems.environment import *
from pygame.locals import *
pygame.init()

def main():
    test = Environment()
    testingString = ""
    for i in range(0, len(test.board[0]), 1):
        testingString = ""
        for j in range(0, len(test.board), 1):
            if test.board[j][i].getPath():
                testingString += " P"
            else:
                testingString += " N"
        print(testingString)

    added = False
    for i in range(0, len(test.board[0]), 1):
        testingString = ""
        for j in range(0, len(test.board), 1):
            for k in range(0, test.pathes[0].pathLength() - 1, 0):
                tempPoint = test.pathes[0].returnPoint(k)
                if tempPoint.getX() == i and tempPoint.getY() == j:
                    testingString += " P"
                    added = True
            if not added:
                testingString += " N"

main()


import pygame, random, sys, time
from pygame.locals import *

# _boardX --> The x dimensions of the grid
# _boardY --> The y dimensions of the grid
class Environment():
    global board, level
    def __init__(self, _boardX, _boardY):
        board = []

        for i in range(0, _boardX, 1):
            board.append([])
            for j in range(0, _boardY, 1):
                board[i].append(SingleGrid())

    def readFile(self, whatLevel):
        global board
        if whatLevel == 0:
            levelOne = open('testMap.txt')

            for line in levelOne:
                board.append(line.rstrip().split(' '))

    def getPath(self):

        randInt = 2

    #Determines if a tower can be placed in the specified position
    def towerPlacement(self, posX, posY):
        randInt = 2

    #Determines the enemy's next step
    def futurePath(self, posX, posY):
        randInt = 2


# What is contained in a single grid point
class SingleGrid():
    global hasTower, hasEnemy, hasPath
    def __init__(self):
        self.hasTower, self.hasEnemy, self.hasPath = False, False, False
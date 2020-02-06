# _boardX --> The x dimensions of the grid
# _boardY --> The y dimensions of the grid
class Environment():
    import pygame, random, sys, time

    global board
    def __init__(self):
        board = []

        self.readFile(0)

    #Opens the map and puts it as the board
    def readFile(self, whatLevel):
        level = []
        if whatLevel == 0:
            levelOne = open('config/maps/testMap.txt')

            for line in levelOne:
                level.append(line.rstrip().split(' '))

        for i in range(0, len(level), 1):
            print(level[i])

        for i in range(0, len(level[0]), 1):
            board.append([])
            for j in range(0, len(level), 1):
                board[i].append(SingleGrid())

        self.createBoard(level)

    #Puts the map into the board array
    def createBoard(self, array):
        global board
        for i in range(0, len(array), 1):
            for j in range(0, len(array[i]), 1):
                #P = Path
                if array[i][j] == "P":
                    board[j][i].changePath(True)
                #E = End
                if array[i][j] == "E":
                    board[j][i].changeEnd(True)

    #Determines if a tower can be placed in the specified position
    def towerPlacement(self, posX, posY):
        randInt = 2

    #Determines the enemy's next step, and takes in the enemy's current x and y
    def futurePath(self, posX, posY):
        tempX, tempY = posX, posY

        endFound = False
        while not endFound:
            if board[tempX][tempY - 1].getPath():
                tempY = tempY - 1
            elif board[tempX][tempY + 1].getPath():
                tempY = tempY + 1
            elif board[tempX - 1][tempY].getPath():
                tempX = tempX - 1
            elif board[tempX + 1][tempY].getPath():
                tempX = tempX + 1


# What is contained in a single grid point
class SingleGrid():
    REQ_ATTRS = ["hasTower", "hasEnemy", "hasPath", "hasEnd"]
    TYPE_ATTRIBUTES = {
        "hasTower" : False,
        "hasEnemy" : False,
        "hasPath" : False,
        "hasEnd" : False
    }

    def getPath(self):
        return self.hasPath

    def changePath(self, newPath):
        self.hasPath = newPath

    def changeEnd(self, newEnd):
        self.hasEnd = newEnd

tester = Environment()
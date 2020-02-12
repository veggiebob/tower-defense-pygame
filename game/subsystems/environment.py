# _boardX --> The x dimensions of the grid
# _boardY --> The y dimensions of the grid
class Environment():
    import pygame, sys

    def __init__(self):
        self.board = []
        self.readFile(0)

    #Opens the map and puts it as the board
    def readFile(self, whatLevel):
        level = []
        if whatLevel == 0:
            levelOne = open('../../config/maps/testMap.txt')

            for line in levelOne:
                level.append(line.rstrip().split(' '))

        for i in range(0, len(level[0]), 1):
            self.board.append([])
            for j in range(0, len(level), 1):
                self.board[i].append(SingleGrid())

        self.createBoard(level)

    #Puts the map into the board array
    def createBoard(self, array):
        for i in range(0, len(array), 1):
            for j in range(0, len(array[i]), 1):
                #P = Path
                if array[i][j] == "P":
                    self.board[j][i].changePath(True)
                #E = End
                if array[i][j] == "E":
                    self.board[j][i].changeEnd(True)

    #Places the tower if it can be placed there
    def placeTower(self, posX, posY):
        if self.adjacentPath(posX, posY):
            self.board[posX][posY].changeTower(True)

    #Determines if a tower can be placed in the specified position
    def adjacentPath(self, posX, posY):
        if self.board[posX][posY - 1].getPath() or self.board[posX][posY - 1].getEnd():
            return True
        elif self.board[posX][posY + 1].getPath() or self.board[posX][posY + 1].getEnd():
            return True
        elif self.board[posX - 1][posY].getPath() or self.board[posX - 1][posY].getEnd():
            return True
        elif self.board[posX + 1][posY].getPath() or self.board[posX + 1][posY].getEnd():
            return True

        return False

    #Determines the enemy's next step, and takes in the enemy's current x and y
    def futurePath(self, posX, posY):
        tempX, tempY = posX, posY

        if self.board[tempX][tempY - 1].getPath() or self.board[tempX][tempY - 1].getEnd():
            tempY = tempY - 1
        elif self.board[tempX][tempY + 1].getPath() or self.board[tempX][tempY + 1].getEnd():
            tempY = tempY + 1
        elif self.board[tempX - 1][tempY].getPath() or self.board[tempX - 1][tempY].getEnd():
            tempX = tempX - 1
        elif self.board[tempX + 1][tempY].getPath() or self.board[tempX + 1][tempY].getEnd():
            tempX = tempX + 1

        #return a point

# What is contained in a single grid point
class SingleGrid():
    REQ_ATTRS = ["hasTower", "hasEnemy", "hasPath", "hasEnd"]
    DEFAULT_ATTRIBUTES = {
        "hasTower" : False,
        "hasEnemy" : False,
        "hasPath" : False,
        "hasEnd" : False
    }
    def __init__(self):
        self.hasTower = False
        self.hasEnemy = False
        self.hasPath = False
        self.hasEnd = False

    def getPath(self):
        return self.hasPath

    def getEnemy(self):
        return self.hasEnemy

    def getTower(self):
        return self.hasTower

    def changeTower(self, newTower):
        self.hasTower = newTower

    def changePath(self, newPath):
        self.hasPath = newPath

    def changeEnd(self, newEnd):
        self.hasEnd = newEnd

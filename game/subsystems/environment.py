class Environment():
    import pygame, sys, random
    from game.common.math import Point

    def __init__(self):
        self.board = []
        self.pathes = []
        self.readFile(0)
        self.createPath()

    # Opens the map and puts it as the board
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

    # Puts the map into the board array
    def createBoard(self, array):
        for i in range(0, len(array), 1):
            for j in range(0, len(array[i]), 1):
                # P = Path
                if array[i][j] == "P":
                    self.board[j][i].changePath(True)
                if array[i][j] == "E":
                    self.board[j][i].changeEnd(True)
                if array[i][j] == "S":
                    self.board[j][i].changeStart(True)

    # Places the tower if it can be placed there
    def placeTower(self, posX, posY):
        if self.adjacentPath(posX, posY):
            self.board[posX][posY].changeTower(True)

    # Determines if a tower can be placed in the specified position
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

    # Determines the enemy's next step, and takes in the enemy's current x and y, previous x, and previous y
    def futurePath(self, posX, posY, pastX, pastY):
        tempX, tempY, canGo = posX, posY, []

        if tempY - 1 != pastY and (self.board[tempX][tempY - 1].getPath() or self.board[tempX][tempY - 1].getEnd()):
            canGo.append(self.Point(tempX, tempY - 1))
        if tempY + 1 != pastY and (self.board[tempX][tempY + 1].getPath() or self.board[tempX][tempY + 1].getEnd()):
            canGo.append(self.Point(tempX, tempY + 1))
        if tempX - 1 != pastX and (self.board[tempX - 1][tempY].getPath() or self.board[tempX - 1][tempY].getEnd()):
            canGo.append(self.Point(tempX - 1, tempY))
        if tempX + 1 != pastX and (self.board[tempX + 1][tempY].getPath() or self.board[tempX + 1][tempY].getEnd()):
            canGo.append(self.Point(tempX + 1, tempY))
        return canGo[self.random.randrange(0, len(canGo), 1)]

    def returnPlaces(self, posX, posY, pastX, pastY):
        tempX, tempY, canGo = posX, posY, []

        if tempY - 1 != pastY and (self.board[tempX][tempY - 1].getPath() or self.board[tempX][tempY - 1].getEnd()):
            canGo.append(self.Point(tempX, tempY - 1))
        if tempY + 1 != pastY and (self.board[tempX][tempY + 1].getPath() or self.board[tempX][tempY + 1].getEnd()):
            canGo.append(self.Point(tempX, tempY + 1))
        if tempX - 1 != pastX and (self.board[tempX - 1][tempY].getPath() or self.board[tempX - 1][tempY].getEnd()):
            canGo.append(self.Point(tempX - 1, tempY))
        if tempX + 1 != pastX and (self.board[tempX + 1][tempY].getPath() or self.board[tempX + 1][tempY].getEnd()):
            canGo.append(self.Point(tempX + 1, tempY))
        return canGo

    # Creates the a list with all the path points
    def createPath(self):
        path, numPathes = Path(), 0
        for i in range(0, len(self.board), 1):
            for j in range(0, len(self.board[i]), 1):
                if self.board[i][j].getStart():
                    path.addPoint(self.Point(i, j))

        lastX, lastY, temp, endsFound = path.returnPoint(0).getX(), path.returnPoint(0).getY(), [], 0
        nowX, nowY = lastX, lastY
        self.pathes.append(path)

        if lastX != 0:
            if self.board[lastX - 1][lastY].getPath():
                self.pathes[0].addPoint(self.Point(lastX - 1, lastY))
        elif lastX != len(self.board):
            if self.board[lastX + 1][lastY].getPath():
                self.pathes[0].addPoint(self.Point(lastX + 1, lastY))
        elif lastY != 0:
            if self.board[lastX][lastY - 1].getPath():
                self.pathes[0].addPoint(self.Point(lastX, lastY - 1))
        elif lastY != len(self.board[lastX]):
            if self.board[lastX][lastY + 1].getPath():
                self.pathes[0].addPoint(self.Point(lastX, lastY + 1))

        counter = 0
        while endsFound < len(self.pathes):
            pathesNum = len(self.pathes)
            for i in range(0, pathesNum, 1):
                nowX = self.pathes[i].returnPoint(self.pathes[i].pathLength() - 1).getX()
                nowY = self.pathes[i].returnPoint(self.pathes[i].pathLength() - 1).getY()
                lastX = self.pathes[i].returnPoint(self.pathes[i].pathLength() - 2).getX()
                lastY = self.pathes[i].returnPoint(self.pathes[i].pathLength() - 2).getY()

                temp = self.returnPlaces(nowX, nowY, lastX, lastY)

                self.pathes[i].addPoint(temp[0])

                if len(temp) > 1:
                    for j in range(1, len(temp), 1):
                        self.pathes.append(self.pathes[i])
                        self.pathes[i + j].addPoint(temp[j])
            endsFound = 0
            for i in range(0, len(self.pathes), 1):
                tempPoint = self.pathes[i].returnPoint(self.pathes[i].pathLength() - 1)
                if self.board[tempPoint.getX()][tempPoint.getY()].getEnd():
                    endsFound += 1

            counter += 1

    # Given a time, returns the position an enemy should be at
    def timeToPos(self, time, pathIndex):
        tempPoint = self.pathes[pathIndex].returnPoint(time)
        nextPoint = self.pathes[pathIndex].returnPoint(time + 1)

        returnX, returnY = tempPoint.getX(), tempPoint.getY()

        if returnX + 1 == nextPoint.getX():
            returnX += time % 1
        elif returnX - 1 == nextPoint.getX():
            returnX -= time % 1
        elif returnY + 1 == nextPoint.getY():
            returnY += time % 1
        elif returnY - 1 == nextPoint.getY():
            returnY -= time % 1

        return self.Point(returnX, returnY)


# What is contained in a single grid point
class SingleGrid():
    REQ_ATTRS = ["hasTower", "hasEnemy", "hasPath", "hasEnd", "hasStart"]
    DEFAULT_ATTRIBUTES = {
        "hasTower": False,
        "hasEnemy": False,
        "hasPath": False,
        "hasEnd": False,
        "hasStart": False
    }

    def __init__(self):
        self.hasTower = False
        self.hasEnemy = False
        self.hasPath = False
        self.hasEnd = False
        self.hasStart = False

    def getPath(self):
        return self.hasPath

    def getEnemy(self):
        return self.hasEnemy

    def getTower(self):
        return self.hasTower

    def getEnd(self):
        return self.hasEnd

    def getStart(self):
        return self.hasStart

    def changeTower(self, newTower):
        self.hasTower = newTower

    def changePath(self, newPath):
        self.hasPath = newPath

    def changeEnd(self, newEnd):
        self.hasEnd = newEnd

    def changeStart(self, newStart):
        self.hasStart = newStart


class Path():
    def __init__(self):
        self.allPoints = []

    def addPoint(self, newPoint):
        self.allPoints.append(newPoint)

    def returnPoint(self, index):
        return self.allPoints[index]

    def pathLength(self):
        return len(self.allPoints)


import pygame, sys
from game.subsystems.environment import *
from pygame.locals import *

pygame.init()

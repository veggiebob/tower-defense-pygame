import pygame, random
from pygame.locals import *
from pygame import *
class BoardVFX:
    def __init__(self, width, height):
        self.board = []
        self.width = width
        self.height = height
        #Array of images here called BGIMAGES that represents all the background images
        #Array of images called VERTROADIMAGES that represents all the different vertical road tiles.
        #Array of images called HORZROADIMAGES that represents all the horizontal road tiles.
        #Array of images called TURNINGIMAGES representing all the images that turn. There is only one turning image for each direction, depending on what the beginning direction is using
        #standard NESW classification (N-1, E-2, S-3 and W-4)
        self.BGIMAGES = []
        self.VERTROADIMAGES = []
        self.HORZROADIMAGES = []
        self.TURNINGIMAGES = []
        readFile()
    def readFile(self, whatLevel = 0):
        level = []
        if whatLevel == 0:
            levelOne = open('../../config/maps/testMap.txt')

            for line in levelOne:
                level.append(line.rstrip().split(' '))
        for i in range(0, len(level[0]), 1):
            self.board.append([])
            for j in range(0, len(level), 1):
                self.board[i].append(level[i][j])

    def drawBackground(self, surf):
        numCols = len(self.board[0])
        numRows = len(self.board)
        for i in range(0,len(self.board)):
            for j in range(0,len(self.board[i])):
                char = self.board[i][j]
                if char == "P":
                    (x, y) = leftTopCoordsOfBox(i, j)
                    dir = determineOrientation(i,j)
                    if dir in ["1","2","3","4"]:
                        surf.blit(self.TURNINGIMAGES[int(dir)-1],(x,y))
                    if dir = "vert":
                        surf.blit(self.VERTROADIMAGES[random.randint(0,2)],(x,y))
                    else:
                        surf.blit(self.HORZROADIMAGES[random.randint(0,2)],(x,y))

    def determineOrientation(self,a,b):
        char = self.board[x][y]
        if self.board[max(x-1,0)][y] == char or self.board[min(x+1,len(self.board))][y] == char:
            if self.board[max(x-1,0)][y] == char and self.board[min(x+1,len(self.board))][y] == char:
                return "vert"
            elif self.board[max(x - 1, 0)][y] == char:
                if self.board[x][min(y+1,len(self.board[0]))] == char:
                    return "1"
                else:
                    return "4"
            else:
                if self.board[x][min(y+1,len(self.board[0]))] ==  char:
                    return "2"
                else:
                    return "3"
        return "horz"
    def leftTopCoordsOfBox(self,x,y):
        return (self.width * x / len(self.board[0]), self.height * y / len(self.board))
import pygame, sys
from game.subsystems.environment import *
from pygame.locals import *
pygame.init()

class Testing ():
    def __init__(self):
        self.test = Environment()
        self.BROWN = (150, 75, 0)
        self.LIGHTBROWN = (181, 101, 29)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.SCREEN = pygame.display.set_mode((50 * len(self.test.board), 50 * len(self.test.board[0])))

    def pathTest(self):
        testingString = ""
        for i in range(0, len(self.test.board[0]), 1):
            testingString = ""
            for j in range(0, len(self.test.board), 1):
                if self.test.board[j][i].getPath():
                    testingString += " P"
                elif self.test.board[j][i].getEnd():
                    testingString += " E"
                elif self.test.board[j][i].getStart():
                    testingString += " S"
                else:
                    testingString += " N"
            print(testingString)

        added = False
        for i in range(0, len(self.test.board[0]), 1):
            testingString = ""
            for j in range(0, len(self.test.board), 1):
                for k in range(0, self.test.pathes[0].pathLength() - 1, 0):
                    tempPoint = self.test.pathes[0].returnPoint(k)
                    tempPoint = self.test.Point(1, 1)
                    if tempPoint.getX() == i and tempPoint.getY() == j:
                        testingString += " P"
                        added = True
                if not added:
                    testingString += " N"

    def timeTest(self):
        pygame.draw.rect(self.SCREEN, self.BROWN, (0,0, 50 * len(self.test.board), 50 * len(self.test.board[0])))

        for i in range(0, len(self.test.board[0]), 1):
            for j in range(0, len(self.test.board), 1):
                if self.test.board[j][i].getPath():
                    pygame.draw.rect(self.SCREEN, self.LIGHTBROWN, (50 * j, 50 * i, 50, 50))
                if self.test.board[j][i].getStart():
                    pygame.draw.rect(self.SCREEN, self.LIGHTBROWN, (50 * j, 50 * i, 50, 50))
                if self.test.board[j][i].getEnd():
                    pygame.draw.rect(self.SCREEN, self.BLACK, (50 * j, 50 * i, 50, 50))

        pygame.display.update()

def main():
    envirTest = Testing()
    # envirTest.timeTest()
    timer = pygame.time
    holdX, holdY = envirTest.test.pathes[0].returnPoint().getX(), envirTest.test.pathes[0].returnPoint().getY()
    while True:
        tempPoint = envirTest.test.timeToPos(timer.get_ticks())
        tempX, tempY = tempPoint.getX(), tempPoint.getY()
        pygame.draw.rect(envirTest.SCREEN, envirTest.LIGHTBROWN, (50 * holdX, 50 * holdY, 50, 50))
        pygame.draw.rect(envirTest.SCREEN, envirTest.BLACK, (50 * tempX, 50 * tempY, 50, 50))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

main()
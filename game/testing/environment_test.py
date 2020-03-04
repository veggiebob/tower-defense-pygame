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
        #Colours
        BROWN = (150, 75, 0)
        LIGHTBROWN = (181, 101, 29)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)

        SCREEN = pygame.display.set_mode((50 * len(self.test.board), 50 * len(self.test.board[0])))
        pygame.draw.rect(SCREEN, BROWN, (0,0, 50 * len(self.test.board), 50 * len(self.test.board[0])))

        for i in range(0, len(self.test.board[0]), 1):
            for j in range(0, len(self.test.board), 1):
                if self.test.board[j][i].getPath():
                    pygame.draw.rect(SCREEN, LIGHTBROWN, (50 * j, 50 * i, 50, 50))
                if self.test.board[j][i].getStart():
                    pygame.draw.rect(SCREEN, LIGHTBROWN, (50 * j, 50 * i, 50, 50))
                if self.test.board[j][i].getEnd():
                    pygame.draw.rect(SCREEN, BLACK, (50 * j, 50 * i, 50, 50))

        pygame.display.update()


def main():
    envirTest = Testing()
    envirTest.timeTest()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

main()
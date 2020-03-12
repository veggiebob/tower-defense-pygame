import pygame, sys
from pygame.locals import *
from game.subsystems.environment import Environment
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

    def timeTest(self):
        pygame.display.update()

def main():
    envirTest = Testing()
    # envirTest.timeTest()
    envirTest.pathTest()

    WHITE = (255, 255, 255)
    BROWN = (150, 75, 0)
    LIGHTBROWN = (181, 101, 29)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    SCREEN = pygame.display.set_mode((25 * len(envirTest.test.board), 25 * len(envirTest.test.board[0])))

    for i in range(0, len(envirTest.test.board[0]), 1):
        for j in range(0, len(envirTest.test.board), 1):
            if envirTest.test.board[j][i].getPath():
                pygame.draw.rect(SCREEN, LIGHTBROWN, (25 * j, 25 * i, 25, 25))
            if envirTest.test.board[j][i].getStart():
                pygame.draw.rect(SCREEN, LIGHTBROWN, (25 * j, 25 * i, 25, 25))
            if envirTest.test.board[j][i].getEnd():
                pygame.draw.rect(SCREEN, BLACK, (25 * j, 25 * i, 25, 25))

    enemyIndex = envirTest.test.enemies[0].getIndex()

    timer = pygame.time
    holdX, holdY = envirTest.test.pathes[0].returnPoint(0).getX(), envirTest.test.pathes[0].returnPoint(0).getY()
    while True:
        tempPoint = envirTest.test.timeToPos(timer.get_ticks() / 1000, 0)
        tempX, tempY = tempPoint.getX(), tempPoint.getY()
        pygame.draw.rect(SCREEN, LIGHTBROWN, (25 * holdX, 25 * holdY, 25, 25))
        pygame.draw.rect(SCREEN, WHITE, (25 * tempX, 25 * tempY, 25, 25))
        holdX, holdY = tempX, tempY
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

main()
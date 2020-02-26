import pygame, sys

from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.environment import *
from game.subsystems.entities import *
from pygame.locals import *
pygame.init()
tester = Environment()
DISPLAYSURF = pygame.display.set_mode((50 * len(tester.board), 50 * len(tester.board[0])))

BROWN = (150, 75, 0)
LIGHTBROWN = (181, 101, 29)
BLACK = (0,0,0)
RED = (255,0,0)
test_yaml = open('./EnemyTest.yaml').read()
BadGuy = YAMLInstancer.get_single(test_yaml, Enemy)

def main():
    global DISPLAYSURF
    clock = pygame.time.Clock()
    now = pygame.time.get_ticks()
    tester.board[BadGuy.xpos][BadGuy.ypos].hasEnemy = True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        timeDifference = pygame.time.get_ticks() - now
        if timeDifference >= BadGuy.moveInterval:
            now = pygame.time.get_ticks()
            tester.board[BadGuy.xpos][BadGuy.ypos].hasEnemy = False
            tempx = tester.futurePath(BadGuy.xpos, BadGuy.ypos, BadGuy.xpast, BadGuy.ypast).getX()
            tempy = tester.futurePath(BadGuy.xpos, BadGuy.ypos, BadGuy.xpast, BadGuy.ypast).getY()
            BadGuy.xpast = BadGuy.xpos
            BadGuy.ypast = BadGuy.ypos
            BadGuy.xpos = tempx
            BadGuy.ypos = tempy
            tester.board[BadGuy.xpos][BadGuy.ypos].hasEnemy = True
            now = pygame.time.get_ticks()
        for x in range(0, len(tester.board)):
            for y in range(0, len(tester.board[0])):
                temp = pygame.Surface((50, 50))
                if tester.board[x][y].getPath() == True:
                    temp.fill(LIGHTBROWN)
                if tester.board[x][y].getPath() != True and tester.board[x][y].hasEnd != True:
                    temp.fill(BROWN)
                if tester.board[x][y].hasEnd == True:
                    temp.fill(BLACK)
                if tester.board[x][y].hasEnemy == True:
                    temp.fill(RED)
                DISPLAYSURF.blit(temp, (x * 50, y * 50))
        pygame.display.update()

main()

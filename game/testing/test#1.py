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
baddiesStr = YAMLInstancer.get_multiple(test_yaml, Enemy)
baddies = []
for enemyStr in baddiesStr:
    baddies.append(baddiesStr[enemyStr])



def main():
    global DISPLAYSURF
    clock = pygame.time.Clock()
    for enemyStart in baddies:
        tester.board[enemyStart.xpos][enemyStart.ypos].hasEnemy = True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        for badGuy in baddies:
            enemyMove(badGuy)
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

def enemyMove(enemy1):
    now = pygame.time.get_ticks()
    timeDifference = now - enemy1.lastmove
    if timeDifference >= enemy1.moveInterval:
        tester.board[enemy1.xpos][enemy1.ypos].hasEnemy = False
        tempx = tester.futurePath(enemy1.xpos, enemy1.ypos, enemy1.xpast, enemy1.ypast).getX()
        tempy = tester.futurePath(enemy1.xpos, enemy1.ypos, enemy1.xpast, enemy1.ypast).getY()
        enemy1.xpast = enemy1.xpos
        enemy1.ypast = enemy1.ypos
        enemy1.xpos = tempx
        enemy1.ypos = tempy
        tester.board[enemy1.xpos][enemy1.ypos].hasEnemy = True
        enemy1.lastmove = pygame.time.get_ticks()

main()

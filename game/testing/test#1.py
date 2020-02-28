import pygame, sys
from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.environment import *
from game.subsystems.entities import *
from pygame.locals import *
pygame.init()
tester = Environment()
DISPLAYSURF = pygame.display.set_mode((50 * len(tester.board), 50 * len(tester.board[0])))
temp = pygame.image.load('Tower.png')
TowerImage = pygame.transform.scale(temp, (50,50))
temp2 = pygame.image.load('Enemy.png')
EnemyImage = pygame.transform.scale(temp2, (50,50))
BROWN = (150, 75, 0)
LIGHTBROWN = (181, 101, 29)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,00)
test_yaml = open('./EnemyTest.yaml').read()
baddiesStr = YAMLInstancer.get_multiple(test_yaml, Enemy)
towertest_yaml = open('./basictower.yaml').read()
Tower = YAMLInstancer.get_single(towertest_yaml, Tower)
baddies = []
projs = []
for enemyStr in baddiesStr:
    baddies.append(baddiesStr[enemyStr])


def main():
    global DISPLAYSURF
    clock = pygame.time.Clock()
    tester.board[Tower.xpos][Tower.ypos].hasTower = True
    for enemyStart in baddies:
        tester.board[enemyStart.xpos][enemyStart.ypos].hasEnemy = True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        for badGuy in baddies:
            enemyMove(badGuy)
            if badGuy.health <= 0:
                baddies.remove(badGuy)
        if len(baddies) == 0:
            test_yaml = open('./EnemyTest.yaml').read()
            baddiesStr = YAMLInstancer.get_multiple(test_yaml, Enemy)
            for enemyStr in baddiesStr:
                baddies.append(baddiesStr[enemyStr])

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
                    temp.blit(EnemyImage, (0,0))
                if tester.board[x][y].hasTower == True:
                    temp.blit(TowerImage, (0,0))
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
    print(projs)


def towerChecks(tower1):
    now = pygame.time.get_ticks()
    timeDifference = now - tower1.lastfire
    if timeDifference >= tower1.reloadSpeed:
        projs.append(tower1.fire(baddies))

main()

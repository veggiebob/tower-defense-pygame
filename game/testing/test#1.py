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
tower1 = YAMLInstancer.get_multiple(towertest_yaml, Tower)
baddies = []
tows = []
projs = []
for enemyStr in baddiesStr:
    baddies.append(baddiesStr[enemyStr])
for towerStr in tower1:
    tows.append(tower1[towerStr])

def main():
    global DISPLAYSURF
    clock = pygame.time.Clock()
    for tower1 in tows:
        tester.board[tower1.xpos][tower1.ypos].hasTower = True
    for enemyStart in baddies:
        tester.board[enemyStart.xpos][enemyStart.ypos].hasEnemy = True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        for tower1 in tows:
            towerChecks(tower1)
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
        for badGuy in baddies:
            enemyMove(badGuy)
            if badGuy.health <= 0:
                baddies.remove(badGuy)
                print(badGuy)
                tester.board[badGuy.xpos][badGuy.ypos].hasEnemy = False
        for proj1 in projs:
            proj1.xpos, proj1.ypos = int(proj1.realX / 50),  int(proj1.realY / 50)
            target1 = proj1.enemy
            ok = False
            for alive in baddies:
                ok = ok or alive == target1
            if not ok:
                projs.remove(proj1)
                print(proj1)
            elif proj1.xpos == proj1.enemy.xpos and proj1.ypos == proj1.enemy.ypos:
                proj1.impact()
                proj1.damage = 0
                proj1.hittimer += 1
                if proj1.hittimer >= 9:
                    projs.remove(proj1)
                    print(proj1)
            else:
                projMove(proj1)
                temp = pygame.Surface((20, 20))
                pygame.draw.circle(temp, GREEN, (10, 10), 10)
                DISPLAYSURF.blit(temp, (proj1.realX, proj1.realY))
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


def projMove(proj1):
    now = pygame.time.get_ticks()
    timeDifference = now - proj1.lastmove
    if timeDifference >= proj1.speed and proj1.hittimer == 0:
        tX, tY = proj1.enemy.xpos * 50, proj1.enemy.ypos * 50
        if proj1.realX > tX:
            proj1.realXs = proj1.realX - 10
        if proj1.realX < tX:
            proj1.realX = proj1.realX + 10
        if proj1.realY > tY:
            proj1.realY = proj1.realY - 10
        if proj1.realY < tY:
            proj1.realY = proj1.realY + 10
        proj1.lastmove = now





def towerChecks(tower1):
    now = pygame.time.get_ticks()
    timeDifference = now - tower1.lastfire
    if timeDifference >= tower1.reloadSpeed:
        projs.append(tower1.fire(baddies))
        tower1.lastfire = now

main()

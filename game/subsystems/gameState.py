import pygame, sys
from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.environment import *
from game.subsystems.entities import *
from pygame.locals import *

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (150, 75, 0)
LIGHTBROWN = (181, 101, 29)

class GameState():
    def __init__(self, mapName):

        global TowerImage, EnemyImage

        temp = pygame.image.load('Tower.png')
        TowerImage = pygame.transform.scale(temp, (50, 50))
        temp2 = pygame.image.load('Enemy.png')
        EnemyImage = pygame.transform.scale(temp2, (50, 50))

        #Arrays for Entities
        self.baddies, self.towers, self.projs = [], [], []

        #In-class time interval tracker
        self.now = 0

        #Class environment object
        self.gameEnv = Environment()

        #Background surface for game
        self.bgSurf = pygame.Surface((50 * len(self.gameEnv.board), 50 * len(self.gameEnv.board[0])))

        #Drawing the background surface
        self.drawBG()


    def drawBG(self):
        for x in range(len(self.gameEnv.board)):
            for y in range(len(self.gameEnv.board[0])):
                temp = pygame.Surface((50, 50))
                boardSpace = self.gameEnv.board[x][y]
                if boardSpace.hasEnd:
                    temp.fill(RED)
                elif boardSpace.getPath():
                    temp.fill(LIGHTBROWN)
                else:
                    temp.fill(BROWN)
                self.bgSurf.blit(temp, (50 * x, 50 * y))


    def enemyAdd(self, enemy1):
        self.baddies.append(enemy1)


    def getEntitiesSurface(self):
        global EnemyImage, TowerImage
        surfaces = []
        for enemy1 in self.baddies:
            temp = pygame.Surface((50 * len(self.gameEnv.board), 50 * len(self.gameEnv.board[0])))
            temp.blit(EnemyImage, (enemy1.xpos * 50, enemy1.ypos * 50))
            surfaces.append(temp)
        for tower1 in self.towers:
            temp = pygame.Surface((50 * len(self.gameEnv.board), 50 * len(self.gameEnv.board[0])))
            temp.blit(TowerImage, (tower1.xpos * 50, tower1.ypos * 50))
            surfaces.append(temp)
        projSurf = pygame.Surface((50 * len(self.gameEnv.board), 50 * len(self.gameEnv.board[0])))
        for proj1 in self.projs:
            temp = pygame.Surface((20, 20))
            pygame.draw.circle(temp, GREEN, (10, 10), 10)
            projSurf.blit(temp, (proj1.realX, proj1.realY))
        surfaces.append(projSurf)
        return surfaces


    def towerAdd(self, tower1):
        self.towers.append(tower1)


    def tick(self, dT):
        self.now += dT

        for tower1 in self.towers:
            self.towerChecks(tower1)

        self.drawBG()

        for proj1 in self.projs:
            proj1.xpos, proj1.ypos = int(proj1.realX / 50), int(proj1.realY / 50)
            target1 = proj1.enemy
            ok = False
            for alive in self.baddies:
                ok = ok or alive == target1
            if not ok:
                self.projs.remove(proj1)
            elif proj1.xpos == proj1.enemy.xpos and proj1.ypos == proj1.enemy.ypos:
                proj1.impact()
                proj1.damage = 0
                proj1.hittimer += 1
                if proj1.hittimer >= 9:
                    self.projs.remove(proj1)
                    print(proj1)
            else:
                self.projMove(proj1)

        for badGuy in self.baddies:
            self.enemyMove(badGuy)

            if badGuy.health <= 0:
                self.baddies.remove(badGuy)
                self.gameEnv.board[badGuy.xpos][badGuy.ypos].hasEnemy = False




    def enemyMove(self, enemy1):
        timeDifference = self.now - enemy1.lastmove
        if timeDifference >= enemy1.moveInterval:
            self.gameEnv.board[enemy1.xpos][enemy1.ypos].hasEnemy = False
            tempx = self.gameEnv.futurePath(enemy1.xpos, enemy1.ypos, enemy1.xpast, enemy1.ypast).getX()
            tempy = self.gameEnv.futurePath(enemy1.xpos, enemy1.ypos, enemy1.xpast, enemy1.ypast).getY()
            enemy1.xpast = enemy1.xpos
            enemy1.ypast = enemy1.ypos
            enemy1.xpos = tempx
            enemy1.ypos = tempy
            self.gameEnv.board[enemy1.xpos][enemy1.ypos].hasEnemy = True
            enemy1.lastmove = self.now

    def projMove(self, proj1):
        timeDifference = self.now - proj1.lastmove
        if timeDifference >= proj1.speed and proj1.hittimer == 0:
            tX, tY = proj1.enemy.xpos * 50, proj1.enemy.ypos * 50
            if proj1.realX > tX:
                proj1.realX = proj1.realX - 10
            if proj1.realX < tX:
                proj1.realX = proj1.realX + 10
            if proj1.realY > tY:
                proj1.realY = proj1.realY - 10
            if proj1.realY < tY:
                proj1.realY = proj1.realY + 10
            proj1.lastmove = self.now

    def towerChecks(self, tower1):
        timeDifference = self.now - tower1.lastfire
        if timeDifference >= tower1.reloadSpeed:
            self.projs.append(tower1.fire(self.baddies))
            tower1.lastfire = self.now





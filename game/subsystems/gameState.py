import copy

import pygame, sys

from game.common.math import Vector
from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.gamer import Shop, Player
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
    def __init__(self, towerImage, enemyImage, scale=50, initial_money=300, initial_health=50):
        
        self.towerImage = towerImage
        self.enemyImage = enemyImage
        self.draw_dim = scale

        #Arrays for Entities
        self.baddies, self.towers, self.projs = [], [], []
        self.shop = Shop(initial_money)
        self.player = Player(initial_health)

        #In-class time interval tracker
        self.now = 0

        self.hovering = 0

        #Class environment object
        self.gameEnv = Environment()

        #Background surface for game
        self.bgSurf = pygame.Surface((self.draw_dim * len(self.gameEnv.board), self.draw_dim * len(self.gameEnv.board[0])))

        #Drawing the background surface
        self.drawBG()

        self.towerHoverImage = pygame.Surface((self.draw_dim, self.draw_dim))
        self.towerHoverImage = self.towerHoverImage.convert_alpha()
        self.towerHoverImage.fill((0, 0, 0, 0))


        self.towerHoverX, self.towerHoverY = 0, 0
        self.holdingTower = None
        self.isHoldingTower = False
        self.mouse_position = Vector()


    def drawBG(self):
        for x in range(len(self.gameEnv.board)):
            for y in range(len(self.gameEnv.board[0])):
                temp = pygame.Surface((self.draw_dim, self.draw_dim))
                boardSpace = self.gameEnv.board[x][y]
                if boardSpace.hasEnd:
                    temp.fill(RED)
                elif boardSpace.getPath():
                    temp.fill(LIGHTBROWN)
                else:
                    temp.fill(BROWN)
                self.bgSurf.blit(temp, (self.draw_dim * x, self.draw_dim * y))
        if self.hovering:
            self.bgSurf.blit(self.towerHoverImage, (self.towerHoverX, self.towerHoverY))

    def enemyAdd(self, enemy1):
        new_enemy = copy.deepcopy(enemy1)
        new_enemy.xpos = self.gameEnv.getAStart().getX()
        new_enemy.xpos = self.gameEnv.getAStart().getY()
        self.baddies.append(new_enemy)


    def getEntitiesSurface(self):
        surfaces = [] # [surface, tupleposition]
        for enemy1 in self.baddies:
            temp = pygame.Surface((self.draw_dim * len(self.gameEnv.board), self.draw_dim * len(self.gameEnv.board[0])))
            temp = temp.convert_alpha()
            temp.fill((0, 0, 0, 0))
            temp.blit(self.enemyImage, (0, 0))
            surfaces.append((temp, (enemy1.getFloatPosition(self.now) * self.draw_dim).to_tuple()))
        for tower1 in self.towers:
            temp = pygame.Surface((self.draw_dim * len(self.gameEnv.board), self.draw_dim * len(self.gameEnv.board[0])))
            temp = temp.convert_alpha()
            temp.fill((0, 0, 0, 0))
            temp.blit(self.towerImage, (0, 0))
            surfaces.append((temp, (tower1.xpos * self.draw_dim , tower1.ypos * self.draw_dim)))

        if self.isHoldingTower:
            temp = pygame.Surface((self.draw_dim * len(self.gameEnv.board), self.draw_dim * len(self.gameEnv.board[0])))
            temp = temp.convert_alpha()
            temp.fill((0, 0, 0, 0))
            temp.blit(self.towerImage, (0, 0))
            surfaces.append((temp, (self.mouse_position.x - self.draw_dim/2, self.mouse_position.y - self.draw_dim/2)))

        projSurf = pygame.Surface((self.draw_dim * len(self.gameEnv.board), self.draw_dim * len(self.gameEnv.board[0])))
        projSurf = projSurf.convert_alpha()
        projSurf.fill((0, 0, 0, 0))
        for proj1 in self.projs:
            if proj1 is None: continue
            temp = pygame.Surface((20, 20))
            temp = temp.convert_alpha()
            temp.fill((0, 0, 0, 0))
            pygame.draw.circle(temp, GREEN, (10, 10), 10)
            projSurf.blit(temp, (proj1.realX, proj1.realY))
        surfaces.append((projSurf, (0, 0)))
        return surfaces


    def towerAdd(self, tower1):
        self.towers.append(tower1)

    def update (self, mouse_position: Vector, mouse_down: bool, mouse_pressed: bool):
        self.towerHoverX, self.towerHoverY = self.mouseToBoard(mouse_position.x, mouse_position.y)
        self.mouse_position = mouse_position
        if mouse_pressed:
            self.drawBG() # just in case
        if not mouse_down:
            if self.isHoldingTower: # you just released a tower
                try:
                    successful = self.gameEnv.placeTower(self.towerHoverX, self.towerHoverY) # todo: actually make this work
                    print('tried to place a tower')
                    if successful:
                        print('operation successful %s, %s'%(self.towerHoverX, self.towerHoverY))
                    else:
                        print('did not place tower %s, %s'%(self.towerHoverX, self.towerHoverY))
                    self.holdingTower.xpos = self.towerHoverX
                    self.holdingTower.ypos = self.towerHoverY
                    self.towerAdd(copy.deepcopy(self.holdingTower))
                except: pass
                self.drawBG()
            self.holdingTower = None
            self.isHoldingTower = False

    def tick(self, dT):
        self.now += dT

        for tower1 in self.towers:
            self.towerChecks(tower1)

        for proj1 in self.projs:
            if proj1 is None: continue
            proj1.xpos, proj1.ypos = int(proj1.realX / self.draw_dim), int(proj1.realY / self.draw_dim)
            target1 = proj1.enemy
            ok = False
            for alive in self.baddies:
                ok = ok or alive == target1
            if not ok:
                self.projs.remove(proj1)
                continue
            elif proj1.xpos == proj1.enemy.xpos and proj1.ypos == proj1.enemy.ypos:
                proj1.impact()
                proj1.damage = 0
                proj1.hittimer += 1
                if proj1.hittimer >= 9:
                    self.projs.remove(proj1)
                    continue
            else:
                self.projMove(proj1)
            if proj1.outOfRange():
                self.projs.remove(proj1)
                continue

        for badGuy in self.baddies:
            self.enemyMove(badGuy)

            if badGuy.health <= 0:
                self.gameEnv.board[badGuy.xpos][badGuy.ypos].hasEnemy = False
                # print('enemy %s died with a health of %d'%(badGuy, badGuy.health))
                self.baddies.remove(badGuy)




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
            if self.gameEnv.getTile(enemy1.xpos, enemy1.ypos).getEnd():
                self.enemyEscaped(enemy1)
                self.baddies.remove(enemy1)


    def enemyEscaped(self, enemy: Enemy) -> None:
        self.player.hit(enemy)

    def projMove(self, proj1):
        v = Vector(proj1.enemy.xpos * self.draw_dim, proj1.enemy.ypos * self.draw_dim) - Vector(proj1.realX, proj1.realY)
        v = v.normalize() * proj1.speed
        proj1.realX += v.x
        proj1.realY += v.y


    def mouseToBoard(self, mX, mY):
        return int((mX - (mX % self.draw_dim)) / self.draw_dim), int((mY - (mY % self.draw_dim)) / self.draw_dim)

    def towerChecks(self, tower1):
        timeDifference = self.now - tower1.lastfire
        if timeDifference >= tower1.reloadSpeed:
            self.projs.append(tower1.fire(self.baddies))
            tower1.lastfire = self.now


    def changeTowerHover(self, newTowerImage):
        self.towerHoverImage = newTowerImage


    def grabTower(self, tower:Tower):
        self.hovering = True
        self.holdingTower = tower
        self.isHoldingTower = True

    def checkGameOver(self) -> bool:
        return self.player.dead






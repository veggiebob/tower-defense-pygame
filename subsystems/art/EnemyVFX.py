import pygame
from pygame.locals import *
pygame.init()
class EnemyVFX:
    def __init__(self):
        self.enemyvisuals = []
        self.enemyNames = []
        self.deathImages = []
    def draw(self, surf,enemyName, frameCount, x, y):
        ind = self.getEnemyIndex(enemyName)
        surf.blit(self.enemyvisuals[ind][frameCount],(x,y))
    def getEnemyIndex(self, enemyName):
        for i in range(0, len(self.enemyNames)):
            if(self.enemyNames[i] == enemyName):
                return i
        return -1
    def drawDeathAnimation(self, enemyName, x, y):
        ind = self.getEnemyIndex(enemyName)
        surf.blit(self.deathImages[ind], (x,y))
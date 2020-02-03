import pygame

class Tower():
    #__init__ takes position as towerPos, a tuple in the format (x, y)
    def __init__(self, towerPos):
        self.xPos = towerPos[0]
        self.yPos = towerPos[1]
        self.imageFilename = ""
        self.image = pygame.image.load(self.imageFilename)
        self.rect = self.image.get_rect()

        self.range = 0
        self.speed = 0

    def fire(self, enemiesList, timeInterval):
        for target in enemiesList:
            if target.futurePosition(timeInterval) <= self.range:
                return Projectile()



class Enemy:
    def __init__(self, _health, _speed, _xpos, _ypos):
        self.health = _health
        self.speed = _speed
        self.xpos = _xpos
        self.ypos = _ypos
        self.isFrozen = False
    def takeDamage(self, damage):
        self.health -= damage
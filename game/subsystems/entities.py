import pygame, yaml

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
    # position is a tuple in the format (x,y)
    REQ_ATTRS = ['health', 'speed', 'xpos', 'ypos', 'isFrozen', 'image', 'rect']
    #Not sure what to call the next line
    TYPE_ATTRS = {
        "health" : int,
        'speed': int,
        'xpos' : int,
        'ypos': int,
        'isFrozen' : bool,
        'image': pygame.surface,
        'rect' : pygame.rect
    }
    DEFAULT_ATTRS = {
        'isFrozen' : False
    }


    def takeDamage(self, damage):
        self.health -= damage


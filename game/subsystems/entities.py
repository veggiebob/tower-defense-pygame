import pygame


class Tower():
    # __init__ takes position as towerPos, a tuple in the format (x, y)

    REQ_ATTRS = ['range', 'fireSpeed', 'xpos', 'ypos', 'reloadSpeed', 'projDamage', 'image', 'rect']

    TYPE_ATTRS = {
        'range': int,
        'fireSpeed': int,
        'xpos': int,
        'ypos': int,
        'reloadSpeed': int,
        'projDamage': int,
        #'image': pygame.Surface,
        #'rect': pygame.Rect
    }

    def fire(self, enemiesList, timeInterval):
        for target in enemiesList:
            if target.futurePosition(timeInterval) <= self.range:
                return Projectile()


class Projectile():

    REQ_ATTRS = ['xpos', 'ypos', 'enemy' 'damage']

    TYPE_ATTRS = {
        'xpos': int,
        'ypos': int,
        #'enemy': Enemy
        'damage': int
    }

    def impact(self):
        self.enemy.takeDamage(self.damage)

class Enemy:
    # position is a tuple in the format (x,y)
    REQ_ATTRS = ['health', 'speed', 'xpos', 'ypos', 'isFrozen', 'image', 'rect']
    #Not sure what to call the next line
    TYPE_ATTRS = {
        "health" : int,
        'speed': int,
        'xpos': int,
        'ypos': int,
        'xpast': int,
        'ypast': int,
        'isFrozen' : bool
        #'image': pygame.Surface,
        #'rect' : pygame.rect
    }
    DEFAULT_ATTRS = {
        'isFrozen' : False
    }


    def takeDamage(self, damage):
        self.health -= damage



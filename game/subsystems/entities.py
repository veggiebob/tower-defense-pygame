import pygame, yaml


class Tower():
    # __init__ takes position as towerPos, a tuple in the format (x, y)

    REQ_ATTRS = ['range', 'fireSpeed', 'xpos', 'ypos', 'reloadSpeed', 'image', 'rect']

    ATTRS_TYPE = {
        'range': int,
        'fireSpeed': int,
        'xpos': int,
        'ypos': int,
        'reloadSpeed': int,
        'image': pygame.Surface,
        'rect': pygame.Rect
    }

    def fire(self, targetEnemies):
        #need to do some aiming stuff here, for now just fires at first enemy in the list
        return Projectile(self.xpos, self.ypos, targetEnemies[0])

class Enemy:
    # position is a tuple in the format (x,y)
    REQ_ATTRS = ['health', 'speed', 'xpos', 'ypos', 'isFrozen', 'image', 'rect']
    # Not sure what to call the next line
    ATTRS_TYPE = {
        "health": int,
        'speed': int,
        'xpos': int,
        'ypos': int,
        'isFrozen': bool,
        'image': pygame.image,
        'rect': pygame.rect
    }

    def takeDamage(self, damage):
        self.health -= damage


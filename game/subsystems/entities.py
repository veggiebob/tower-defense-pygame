import pygame, yaml


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

    def fire(self, targetEnemies):
        #need to do some aiming stuff here, for now just fires at first enemy in the list
        return Projectile(self.xpos, self.ypos, targetEnemies[0], self.projDamage)


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
        'isFrozen' : bool,
        'image': pygame.surface,
        'rect' : pygame.rect
    }
    DEFAULT_ATTRS = {
        'isFrozen' : False
    }


    

    def takeDamage(self, damage):
        self.health -= damage



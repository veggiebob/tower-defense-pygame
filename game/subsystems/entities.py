import pygame


class Tower():
    # __init__ takes position as towerPos, a tuple in the format (x, y)

    REQ_ATTRS = ['range', 'fireSpeed', 'xpos', 'ypos', 'reloadSpeed', 'projDamage']

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

    def fire(self, enemiesList):
        for target in enemiesList:
            if ((target.xpos - self.xpos) ^ 2) + ((target.ypos - self.ypos) ^ 2) <= self.range:
                return Projectile(self.xpos, self.ypos, target, self.projDamage)


class Projectile():
    def __init__(self, x, y, target, damageAmt):
        self.xpos, self.ypos = x, y
        self.enemy = target
        self.damage = damageAmt
    def impact(self):
        self.enemy.takeDamage(self.damage)

class Enemy:
    # position is a tuple in the format (x,y)
    REQ_ATTRS = ['health', 'speed', 'xpos', 'ypos']
    #Not sure what to call the next line
    TYPE_ATTRS = {
        "health" : int,
        'speed': int,
        'xpos': int,
        'ypos': int,
        #'isFrozen' : bool,
        #'image': pygame.Surface,
        #'rect' : pygame.rect
    }

    #DEFAULT_ATTRS = {
    #    'isFrozen' : False
    #}


    def takeDamage(self, damage):
        self.health -= damage

    def __str__(self):
        return("Health: " + str(self.health) + "\n" + "X, Y: " + str(self.xpos) + ", " + str(self.ypos) + "\n" + "speed: " + str(self.speed) + "\n" )

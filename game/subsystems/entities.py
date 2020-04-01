import math
from game.common.math import Vector


class Tower():
    # __init__ takes position as towerPos, a tuple in the format (x, y)

    REQ_ATTRS = ['range', 'fireSpeed', 'xpos', 'ypos', 'reloadSpeed', 'projDamage', 'projSpeed', 'lastfire', 'price']

    TYPE_ATTRS = {
        'range': int,
        'fireSpeed': int,
        'xpos': int,
        'ypos': int,
        'reloadSpeed': int,
        'projDamage': int,
        'projSpeed': int,
        'lastfire': int,
        'price': int
        #'image': pygame.Surface,
        #'rect': pygame.Rect
    }

    def fire(self, enemiesList):
        targetDistance = self.range ** 2
        targetToUse = None

        for target in enemiesList:
            distSquared = ((self.xpos - target.xpos) ** 2) + ((self.ypos - target.ypos) ** 2)
            # print(distSquared)
            if distSquared < targetDistance:
                targetDistance = distSquared
                targetToUse = target

        if targetToUse is None:
            return None

        return Projectile(self.xpos, self.ypos, targetToUse, self.projDamage, self.projSpeed, self.range)


class Projectile():
    def __init__(self, x, y, target, damageAmt, projSpeed, max_range=99999999999):
        self.xpos, self.ypos = x, y
        self.max_range = max_range
        self.setRealPos(self.xpos * 50, self.ypos * 50) # todo: aaaaaaaaaaa
        self.enemy = target
        self.damage = damageAmt
        self.speed = projSpeed
        self.lastmove = 0
        self.hittimer = 0
    def outOfRange(self):
        return math.sqrt((self.realX-self.start_x)**2 + (self.realY-self.start_y)**2) > self.max_range
    def impact(self):
        self.enemy.takeDamage(self.damage)
    def setRealPos(self, rX, rY):
        self.realX, self.realY = rX, rY
        self.start_x, self.start_y = rX, rY

class Enemy:
    health: int
    moveInterval: int
    money: int
    # position is a tuple in the format (x,y)
    REQ_ATTRS = [
        'health',
        'moveInterval',
        # 'xpos',
        # 'ypos',
        # 'xpast',
        # 'ypast',
        # 'lastmove',
        'money'
    ]
    #Not sure what to call the next line
    TYPE_ATTRS = {
        "health" : int,
        'moveInterval': int,
        'xpos': int,
        'ypos': int,
        'xpast': int,
        'ypast': int,
        'lastmove': int,
        'money': int
        #'image': pygame.Surface,
        #'rect' : pygame.rect
    }
    def yaml_init (self):
        self.xpos = 0
        self.ypos = 0
        self.xpast = 0
        self.ypast = 0
        self.lastmove = 0
        self.originalHealth = self.health
    def takeDamage(self, damage):
        self.health -= damage

    def getLoopTime(self, current_time):
        return (current_time - self.lastmove) / self.moveInterval

    def getFloatPosition(self, current_time) -> Vector:
        return Vector(self.xpast, self.ypast) + Vector(self.xpos-self.xpast, self.ypos-self.ypast) * self.getLoopTime(current_time)

    def __str__(self):
        return "Health: " + str(self.health) + "\n" + "X, Y: " + str(self.xpos) + ", " + str(self.ypos) + "\n" + "speed: " + str(self.moveInterval)

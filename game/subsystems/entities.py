import pygame

class Tower():
    #__init__ takes position as towerPos, a tuple in the format (x, y)
    def __init__(self, towerPos):
        self.xPos = towerPos[0]
        self.yPos = towerPos[1]
        self.imageFilename = ""
        self.image = pygame.image.load(self.imageFilename)

        self.range = 0
        self.projSpeed = 0

    def fire(self, enemiesList, enemiesFuturePositions, timeInterval):
        for enemyNum in range(len(enemiesList)):
            if enemiesFuturePositions <= self.range:
                return Projectile()




class Projectile():

    def __init__(self, initialPos, targetEnemy, projSpeed, projDamageAmt):
        self.xPos = initialPos[0]
        self.yPos = initialPos[1]

        self.speed = projSpeed
        self.damageAmt = projDamageAmt

        self.target = targetEnemy

        self.imageFilename = ""
        self.image = pygame.image.load(self.imageFilename)

    def impact(self):
        self.target.takeDamage(self.damageAmt)
import pygame,math
from pygame.locals import *
pygame.init()
class Bullet:
    def __init__(self,imageName):
        self.image = pygame.transform.scale(pygame.image.load("%s.jpg" %imageName), (40,40))
        self.altImage = pygame.transform.scale(pygame.image.load("%s.jpg" %imageName), (40,40))
        self.rect = self.image.get_rect()
        self.center = (0,0)
    def rotateImage(self, a, b):
        (x,y) = a
        (x1,y1) = b
        angle = math.degrees(math.atan2(x-x1, y-y1))
        self.altImage = pygame.transform.rotate(self.image, angle - math.pi/2)
        # rect = self.image.get_rect()
        # rect.center = self.rect.center
        # self.rect = rect
    def update(self,point):
        # self.rect.center = point
        self.center = point
    def draw(self, screen):
        (x,y) = self.center
        rect = Rect(x-20,y-20, 40, 40)
        screen.blit(self.altImage,rect)
    def getCenter(self):
        # return self.rect.center
        return self.center



class TowerVFX:
    def __init__(self,names):
        towerimages = []
        self.names = names
        gunimages = []


    def place(self, surf, name):
        ind = self.getEnemyIndex(name)
        surf.blit(self.toweriamges[ind],(0,0))


    def getEnemyIndex(self, enemyName):
        for i in range(0, len(self.names)):
            if(self.names[i] == enemyName):
                return i
        return -1
class GunVFX:
    def __init__(self,names):
        self.gunimages = []
        for i in range(0,5):
            image = pygame.image.load("gunimage%i" %i).convert_alpha()
            image.set_colorkey((255,255,255))
            self.gunimages.append(image)
        self.firingimages = []
        for i in range(0,5):
            image = pygame.image.load("firingimage%i"%i).convert_alpha()
            image.set_colorkey((255,255,255))
            self.firingimages.append(image)
        self.names = names
        self.angle = 0
    def place(self,surf,name):
        ind = self.getEnemyIndex(name)
        surf.blit(self.gunimages[ind],(0,0))
    def rotate(self,towerName,startingPoint,finalPoint,surf):
        towerVFX = TowerVFX()
        TowerVFX.place(surf, towerName)
        ind = towerVFX.getEnemyIndex[towerName]
        surf.blit(self.getRotatedImage(self.gunimages[ind]), (0,0))
    def getRotatedImage(self, image, a, b):
        (x,y) = a
        (x1,y1) = b
        self.angle = math.degrees(math.atan2(x-x1, y-y1))
        altImage = pygame.transform.rotate(image, self.angle - math.pi/2)
        return altImage
        # rect = self.image.get_rect()
        # rect.center = self.rect.center
        # self.rect = rect
    def fire(self,towerName,surf):
        ind = self.getEnemyIndex(towerName)
        image = pygame.transform.rotate(self.firingimages[ind],self.angle - math.pi/2)
        surf.blit(image,(0,0))
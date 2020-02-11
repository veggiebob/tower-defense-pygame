import pygame,math
from pygame.locals import *
class Bullet(pygame.sprite.Sprite):
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


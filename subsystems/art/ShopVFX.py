import pygame
class ShopVFX:
    def __init__(self,numTowers, names,numTowers):
        self.names =  names
        self.lightenedimages = []
        self.darkenedimages = []
        for i in range(0,len(numTowers)):
            self.lightenedtowers.append(pygame.image.load(".../config/art/lightenedtower%i.jpg"%names[i]))
            self.darkenedtowers.append(pygame.image.load(".../config/art/darkenedtower%i.jpg"%names[i]))
        self.playbuttons = []
        self.pausebuttons = []
        for i in range(0,2):
            #0/1 is like a binary representing whether or not it's darkened
            self.playbuttons.append(pygame.image.load(".../config/art/playbutton%i.jpg"%i))
            self.pausebuttons.append(pygame.image.load(".../config/art/pausebutton%i.jpg"%i))
    def getImage(self,name):
        for i in range(0,len(self.names)):
            nombre = self.names[i]
            if name == nombre:
                if i <len(self.lightenedTowers):
                    return self.lightenedTowers[i]
                if(i == len(self.lightenedTowers)): #index of the play button.
                    return self.playbuttons[0]
                if(i == len(self.lightenedTowers + 1)):
                    return self.pausebuttons[0]
    def getDarkenedImage(self,name):
        for i in range(0,len(self.names)):
            nombre = self.names[i]
            if name == nombre:
                if i <len(self.darkenedTowers):
                    return self.darkenedTowers[i]
                if(i == len(self.darkenedTowers)): #index of the play button.
                    return self.playbuttons[1]
                if(i == len(self.darkenedTowers + 1)):
                    return self.pausebuttons[1]
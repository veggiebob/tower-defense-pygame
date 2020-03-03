import pygame, sys
from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.environment import *
from game.subsystems.entities import *
from pygame.locals import *

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (150, 75, 0)
LIGHTBROWN = (181, 101, 29)

class GameState():
    def __init__(self, mapName):

        #Arrays for Entities
        self.baddies, self.towers, self.projs = []

        #In-class time interval tracker
        self.now = 0

        #Class environment object
        self.gameEnv = Environment()

        #Background surface for game
        self.bgSurf = pygame.Surface((50 * len(self.gameEnv.board), 50 * len(self.gameEnv.board[0])))


        #Drawing the background surface
        for x in range(len(self.gameEnv.board)):
            for y in range(len(self.gameEnv.board[0])):
                temp = pygame.Surface((50, 50))
                boardSpace = self.gameEnv.board[x][y]
                if boardSpace.hasEnd:
                    temp.fill(RED)
                elif boardSpace.getPath():
                    temp.fill(LIGHTBROWN)
                else:
                    temp.fill(BROWN)
                self.bgSurf.blit(temp, (50 * x, 50 * y))

    def tick(self, dT):
        self.now += dT






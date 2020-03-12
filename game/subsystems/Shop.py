import pygame, sys
from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.environment import *
from game.subsystems.entities import *
from pygame.locals import *


class Shop:

    def __init__ (self):
        self.bank = 300

    def buy(self, Tower):
        self.bank -= Tower.price

    def makeMoney(self, Enemy):
        self.bank += Enemy.money
    
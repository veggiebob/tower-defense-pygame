import pygame, sys

from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.environment import *
from game.subsystems.entities import *
from pygame.locals import *
from game.common.math import *

BROWN = (150, 75, 0)
LIGHTBROWN = (181, 101, 29)
BLACK = (0,0,0)
RED = (255,0,0)

env = Environment()
DISPLAYSURF = pygame.display.set_mode((100 * len(env.board), 100 * len(env.board[0])))

test_yaml = open('./towerTest.yaml').read()
test_yaml2 = open('./towerTestEnemy.yaml').read()
tower1 = YAMLInstancer.get_single(test_yaml, Tower)
enemy1 = YAMLInstancer.get_single(test_yaml2, Enemy)
proj1 = tower1.fire([enemy1])
print(enemy1)
if not proj1 is None:
    proj1.impact()
print(enemy1)


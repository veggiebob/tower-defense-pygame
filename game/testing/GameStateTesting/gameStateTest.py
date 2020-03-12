import pygame, sys
from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.entities import *
from pygame.locals import *
from game.subsystems.gameState import *


def main():
    enemyYaml = open('./testEnemies.yaml').read()
    towerYaml = open('./testTowers.yaml').read()

    gameState1 = GameState(5)

    enemiesDict = YAMLInstancer.get_multiple(enemyYaml, Enemy)
    towersDict = YAMLInstancer.get_multiple(towerYaml, Tower)

    for enemyStr in enemiesDict:
        gameState1.enemyAdd(enemiesDict[enemyStr])

    for towerStr in towersDict:
        gameState1.towerAdd(towersDict[towerStr])

    pygame.init()

    displaySurf = pygame.display.set_mode((50 * len(gameState1.gameEnv.board), 50 * len(gameState1.gameEnv.board[0])))

    while True:

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        displaySurf.blit(gameState1.bgSurf, (0, 0))
        for entSurf in gameState1.getEntitiesSurface():
            displaySurf.blit(entSurf, (0, 0))

        pygame.display.update()

main()
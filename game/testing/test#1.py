import pygame
from game.subsystems.environment import *
from game.subsystems.entities import *

tester = Environment()
DISPLAYSURF = pygame.display.set_mode((100 * len(tester.board), 100 * len(tester.board[0])))

BROWN = (150, 75, 0)
LIGHTBROWN = (181, 101, 29)
BLACK = (0,0,0)

def main():
    print(str(len(tester.board)))
    print(str(len(tester.board[0])))
    while True:
        for x in range (0, len(tester.board)):
            for y in range (0, len(tester.board[0])):
                temp = pygame.Surface((100, 100))
                if tester.board[x][y].getPath() == True:
                    temp.fill(LIGHTBROWN)
                if tester.board[x][y].getPath() != True and tester.board[x][y].hasEnd != True:
                    temp.fill(BROWN)
                if tester.board[x][y].hasEnd == True:
                    temp.fill(BLACK)
                DISPLAYSURF.blit(temp, (x * 100, y*100))
        pygame.display.update()
        

main()

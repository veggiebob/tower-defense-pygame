import sys
from game.subsystems.ui.elements.buttons import *
from pygame.locals import *
pygame.init()
Text.DEFAULT_TEXT = Text('../common/verdana.ttf')

display = pygame.display.set_mode((100, 100))
button = Button(Vector(0, 0), Vector(50, 50), "hello world")

mouse_position = Vector(0, 0)
mouse_down = False
mouse_pressed = False
while True:
    mouse_pressed = not 1
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == MOUSEMOTION:
            mouse_position = Vector.from_tuple(e.pos)
        elif e.type == MOUSEBUTTONDOWN:
            mouse_down = True
            mouse_pressed = True
        elif e.type == MOUSEBUTTONUP:
            mouse_down = False
    button.update(mouse_position, mouse_down, mouse_pressed)
    button.draw_on_surface(display)
    pygame.display.update()
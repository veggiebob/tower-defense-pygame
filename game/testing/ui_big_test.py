from game.common.math import Vector
from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.ui.graphical_user_interface import GUI
from game.subsystems.ui.layout.layout import Layout
from game.subsystems.ui.layout.layoutmanager import LayoutManager
from game.subsystems.ui.layout.panel import Panel
from game.common.text import Text
import pygame, sys

from game.subsystems.ui.ui_handler import ElementsHandler

pygame.init()
Text.DEFAULT_TEXT = Text("../common/verdana.ttf")

yaml_layout = open("big_layout_test.yaml").read() # start menu layout

# with or without using the class notation, get the instance
panel = YAMLInstancer.get_single(yaml_layout, Panel)
# using a method to get a flattened version of all the panels from tree form (most likely you won't be doing this)
inner_panels = panel.get_all_inner()
print('flattened layout:')
print(';\n'.join([str(p) for p in inner_panels])) # some debug (print the panels from yaml)

# create a layout to hold the panels
layout = Layout.fromPanelList(inner_panels)
# setup some pygame stuff
WIDTH, HEIGHT = 400, 400
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
DISPLAY.fill((0, 0, 0))
# map the panels onto the screen
screen_panels = layout.getPanelsOnRect((0, 0, WIDTH, HEIGHT))

#gui
layout_manager = LayoutManager()
layout_manager.addLayout(layout, 'main')
layout_manager.setCurrentLayout('main')
elements_handler = ElementsHandler.from_panel_list(screen_panels)
print('all elements: %s'%elements_handler.get_elements())
gui = GUI(elements_handler, layout_manager)

# update / handle exiting
mouse_position = Vector(0, 0)
mouse_down = False
mouse_pressed = False
while True:
    mouse_pressed = False
    for e in pygame.event.get():
        if e.type == pygame.MOUSEMOTION:
            mouse_position = Vector(e.pos[0], e.pos[1])
        elif e.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
            mouse_down = True
        elif e.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
        elif e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    gui.update(mouse_position, mouse_down, mouse_pressed)
    gui.draw_to_surface(DISPLAY)
    pygame.display.update()
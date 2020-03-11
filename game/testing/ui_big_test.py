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
WIDTH, HEIGHT = 400, 400
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

yaml_layout = open("big_layout_test.yaml").read() # start menu layout
panel_layouts = YAMLInstancer.get_multiple(yaml_layout, Panel, debug=False)
layout_manager = LayoutManager()
for panel_name, panel_layout in panel_layouts.items():
    layout = Layout.layoutFromPanel(panel_layout)
    layout_manager.addLayout(layout, panel_name)
layout_manager.setCurrentLayout('game_screen')
layout = layout_manager.getLayout('game_screen')
screen_panels = layout.getPanelsOnRect((0, 0, WIDTH, HEIGHT))
elements_handler = ElementsHandler.from_panel_list(screen_panels)
print('all elements: %s'%elements_handler.get_elements())
gui = GUI(elements_handler, layout_manager)
# gui.change_layout('game_screen')

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
    DISPLAY.fill((100, 100, 100))
    gui.update(mouse_position, mouse_down, mouse_pressed)
    gui.draw_to_surface(DISPLAY, draw_panel_borders=True)
    pygame.display.update()
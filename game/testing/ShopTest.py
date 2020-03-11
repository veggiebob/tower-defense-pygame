from game.common.math import Vector
from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.ui.graphical_user_interface import GUI
from game.subsystems.ui.layout.layout import Layout
from game.subsystems.ui.layout.layoutmanager import LayoutManager
from game.subsystems.ui.layout.panel import Panel
from game.common.text import Text
from game.subsystems.gameState import *
import pygame, sys
from game.subsystems.ui.ui_handler import ElementsHandler

pygame.init()
Text.DEFAULT_TEXT = Text("../common/verdana.ttf")
WIDTH, HEIGHT = 1000, 1000
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

yaml_layout = open("Shoptest.yaml").read() # start menu layout
panel_layouts = YAMLInstancer.get_multiple(yaml_layout, Panel, debug=False)
layout_manager = LayoutManager()
for panel_name, panel_layout in panel_layouts.items():
    layout = Layout.layoutFromPanel(panel_layout)
    layout_manager.addLayout(layout, panel_name, set_current=True)

screen_panels = layout.getPanelsOnRect((0, 0, WIDTH, HEIGHT))
elements_handler = ElementsHandler.from_panel_list(screen_panels)
print('all elements: %s'%elements_handler.get_elements())
gui = GUI(elements_handler, layout_manager)

daGame = GameState("TestMap2.txt")

# update / handle exiting
mouse_position = Vector(0, 0)
mouse_down = False
mouse_pressed = False

test_yaml = open('./enemy2.yaml').read()
baddiesStr = YAMLInstancer.get_multiple(test_yaml, Enemy)
towertest_yaml = open('./Tower2.yaml').read()
tower1 = YAMLInstancer.get_multiple(towertest_yaml, Tower)
for enemyStr, v in baddiesStr.items():
    daGame.enemyAdd(v)
for towerStr, v in tower1.items():
    daGame.towerAdd(v)
fps = 30
while True:
    clock = pygame.time.Clock()
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
    clock.tick(30)
    daGame.tick(30)
    DISPLAY.fill((100, 100, 255))
    DISPLAY.blit(daGame.bgSurf, (0,0))
    surfaces = daGame.getEntitiesSurface()
    for each in surfaces:
        DISPLAY.blit(each, (0, 0))
    gui.update(mouse_position, mouse_down, mouse_pressed)
    gui.draw_to_surface(DISPLAY)
    pygame.display.update()
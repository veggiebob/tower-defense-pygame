from game.common.math import Vector, constrain
from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.ui.elements.buttons import Button
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
WIDTH, HEIGHT = 800, 600
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

# SETUP ENTITIES
enemies = list(YAMLInstancer.get_multiple(open('EnemyTest.yaml').read(), Enemy).values())

yaml_layout = open("Shoptest.yaml").read() # start menu layout
panel_layouts = YAMLInstancer.get_multiple(yaml_layout, Panel, debug=False) # get a dictionary with all the layouts
layout_manager = LayoutManager()
for panel_name, panel_layout in panel_layouts.items():
    layout = Layout.layoutFromPanel(panel_layout)
    layout_manager.addLayout(layout, panel_name, set_current=True)
layout = layout_manager.getLayout()
screen_panels = layout.getPanelsOnRect((0, 0, WIDTH, HEIGHT))
elements_handler = ElementsHandler.from_panel_list(screen_panels)
print('all elements: %s'%elements_handler.get_elements())
gui = GUI(elements_handler, layout_manager)

daGame = GameState("TestMap2.txt")

###SETTING ONCLICKS
tower_column = gui.get_element('tower_column')
nb = Button(text="hello world!", tint=Color(255, 0, 0))
nb.name = 'yeet'
tower_column.add_element(nb)
e = tower_column.get_element_by_index(0)
e.set_on_click_listener(lambda self, **kwargs: kwargs['gamestate'].grabTower(kwargs['tower']))
tower1DefYaml = open('./shopBlankTower1.yaml').read()
tower1Blank = YAMLInstancer.get_single(tower1DefYaml, Tower)
e.set_click_args({
    'gamestate': daGame,
    'tower': tower1Blank, #todo: make this the tower that this one contains
})

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
gtime = 0
difficulty = 1
def difficulty_to_enemy (diff=0):
    e = enemies[constrain(int(diff), 0, len(enemies) - 1)]
    print('enemy:')
    print(e)
    return e
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
    gtime += 1
    clock.tick(30)
    daGame.tick(30)
    if gtime%100 == 0: # start a wave
        difficulty += 1
        print('starting wave %d'%difficulty)
        for a in range(0, difficulty):
            daGame.enemyAdd(difficulty_to_enemy(difficulty))
    daGame.update(mouse_position, mouse_down, mouse_pressed)
    DISPLAY.fill((100, 100, 255))
    DISPLAY.blit(daGame.bgSurf, (0,0))
    surfaces = daGame.getEntitiesSurface()
    for each in surfaces:
        DISPLAY.blit(*each)
    gui.update(mouse_position, mouse_down, mouse_pressed)
    gui.draw_to_surface(DISPLAY, draw_panel_borders=True)
    pygame.display.update()
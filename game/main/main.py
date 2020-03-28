from game.common.math import Vector, constrain
from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.ui.elements.buttons import Button, TextView
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

# config
CONFIG_DIR = "../../config/"
GET_CONFIG = lambda filename: open(CONFIG_DIR + filename, 'r')
GET_YAML = lambda filename: GET_CONFIG(filename + '.yaml').read()

# SETUP ENTITIES
enemies = list(YAMLInstancer.get_multiple(GET_YAML('entities/enemies'), Enemy).values())

# make the layout manager
layout_manager = LayoutManager()
# get the layouts
panel_layouts = YAMLInstancer.get_multiple(GET_YAML('layouts'), Panel, debug=False) # get a dictionary with all the layouts
for pn, p in panel_layouts.items():
    p: Panel = p # tell it that p is a panel
    #print('panels: %s'%p.get_all_inner())
    layout = Layout.layoutFromPanel(p) # get the layout
    #print('layout gotten: %s, its panels: %s'%(layout, layout.panels))
    screen_panels = layout.getPanelsOnRect((0, 0, WIDTH, HEIGHT)) # transform panels so that they're on the screen size
    elements_handler = ElementsHandler.from_panel_list(screen_panels) # get the elements from those panels
    #print('elements handler elements: %s'%elements_handler.get_elements())
    layout_manager.addLayout(layout, elements_handler, name=pn, set_current=True)
gui = GUI(layout_manager)

SCALE = 50
TowerImage = pygame.transform.scale(pygame.image.load('%s/entities/temp_assets/Tower.png'%CONFIG_DIR), (SCALE,) * 2)
EnemyImage = pygame.transform.scale(pygame.image.load('%s/entities/temp_assets/Enemy.png'%CONFIG_DIR), (SCALE,) * 2)
daGame = GameState(towerImage=TowerImage, enemyImage=EnemyImage, scale=SCALE) # todo: from yaml things?

###SETTING ONCLICKS
tower_column = gui.get_element('tower_column')
money_element:TextView = gui.get_element('money')
health_element:TextView = gui.get_element('health')
all_towers = list(YAMLInstancer.get_multiple(GET_YAML('entities/towers'), Tower).values())
index = -1
for e in tower_column.get_elements():
    index += 1
    #print('button element is %s'%e)
    e.set_on_click_listener(lambda self, **kwargs: kwargs['gamestate'].grabTower(kwargs['tower']))
    e.set_click_args({
        'gamestate': daGame,
        'tower': all_towers[index]
    })

# update / handle exiting
mouse_position = Vector(0, 0)
mouse_down = False
mouse_pressed = False

fps = 30
gtime = 0
difficulty = 1
def difficulty_to_enemy (diff=0):
    e = enemies[constrain(int(diff), 0, len(enemies) - 1)]
    #print('enemy:')
    #print(e)
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
    daGame.update(mouse_position, mouse_down, mouse_pressed)
    if gtime%100 == 0: # start a wave
        difficulty += 1
        #print('starting wave %d'%difficulty)
        for a in range(0, difficulty):
            daGame.enemyAdd(difficulty_to_enemy(difficulty))
    DISPLAY.fill((100, 100, 255))
    DISPLAY.blit(daGame.bgSurf, (0,0))
    surfaces = daGame.getEntitiesSurface()
    for each in surfaces:
        DISPLAY.blit(*each)
    gui.update(mouse_position, mouse_down, mouse_pressed)
    gui.draw_to_surface(DISPLAY, draw_panel_borders=True)
    money_element.text = "$%s"%daGame.shop.bank
    health_element.text = "%shp"%daGame.player.health
    pygame.display.update()
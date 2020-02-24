from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.ui.layout.layout import Layout
from game.subsystems.ui.layout.panel import Panel
from game.common.text import DEFAULT_TEXT
import pygame, sys
pygame.init()

# should be in it's own file, but this was easier for debugging purposes
yaml_layout = """
start_screen:
  x: 0
  y: 0
  width: 1.0
  height: 1.0
  inner_panels:
    - name: top panel # set name using 'name' property, to an anonymous object
      x: 0
      y: 0
      height: 0.5 # these are in the parent's "field space" so that 0.5 means 50% of the parent panel
      width: 1.0
    - bottom_panel: # set name by making it an object with a key
        x: 0
        y: 0.5
        width: 1.0
        height: 0.5
        inner_panels:
        - bottom_left_panel: {x: 0, y: 0, width: 0.5, height: 1.0} # object in scrunched form
        - {x: 0.5, y: 0, width: 0.5, height: 1.0} # no name property anywhere; reverts to default
"""
# yaml_layout = open("../../config/layouts.yaml").read() # start menu layout

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

# draw stuff
visual_border = 2
for p in screen_panels:
    # draw the panels on the screen
    r = p.get_rect(border=visual_border)
    pygame.draw.rect(DISPLAY, (255, 255, 255), r, 1)
    # display text in the middle
    DEFAULT_TEXT.draw_to_surface(DISPLAY, (r[0] + r[2] * 0.5, r[1] + r[3] * 0.5), p.name, 10, (255, 255, 255))

# update / handle exiting
while True:
    if len([e for e in pygame.event.get() if e.type==pygame.QUIT]) > 0:
        pygame.quit()
        sys.exit()
    pygame.display.update()
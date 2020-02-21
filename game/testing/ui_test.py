from game.common.yaml_parsing import YAMLInstancer
from game.subsystems.ui.layout.layout import Layout
from game.subsystems.ui.layout.panel import Panel
from game.common.text import Text
import pygame, sys
pygame.init()
yaml_layout = """
start_screen:
  x: 0
  y: 0
  width: 1.0
  height: 1.0
  inner_panels:
    - name: top panel
      x: 0
      y: 0
      height: 0.5
      width: 1.0
    - bottom_panel:
        x: 0
        y: 0.5
        width: 1.0
        height: 0.5
        inner_panels:
        - bottom_left_panel: {x: 0, y: 0, width: 0.5, height: 1.0}
        - {x: 0.5, y: 0, width: 0.5, height: 1.0}
"""

# with or without using the class notation, get the instance
panel = YAMLInstancer.get_single(yaml_layout, Panel)
# print(panel)
# print(panel.dump_inner_panels())
inner_panels = panel.get_all_inner()
print('flattened layout:')
print(';\n'.join([str(p) for p in inner_panels]))

layout = Layout.fromPanelList(inner_panels)
WIDTH, HEIGHT = 400, 400
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
DISPLAY.fill((0, 0, 0))
screen_panels = layout.getPanelsOnRect((0, 0, WIDTH, HEIGHT))

T = Text('../common/verdana.ttf')
visual_border = 2
for p in screen_panels:
    r = p.get_rect(border=visual_border)
    pygame.draw.rect(DISPLAY, (255, 255, 255), r, 1)
    T.draw_to_surface(DISPLAY, (r[0] + r[2] * 0.5, r[1] + r[3] * 0.5), p.name, 10, (255, 255, 255))

while True:
    if len([e for e in pygame.event.get() if e.type==pygame.QUIT]) > 0:
        pygame.quit()
        sys.exit()
    pygame.display.update()
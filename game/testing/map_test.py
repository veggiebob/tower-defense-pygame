from pytmx.util_pygame import load_pygame
import pygame, sys
pygame.init()

WIDTH = 400
HEIGHT = 400
display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
display.fill((0, 0, 0))
tiled_map = load_pygame('test_bigger.tmx')
map_scale = 1/2
surfs = []
layer = tiled_map.layers[0]
tile_width = 0
tile_height = 0
for x, y, image in layer:
    img = tiled_map.get_tile_image(x, y, 0)
    # print('x: %s, y: %s, image: %s'%(x, y, img))
    # print('width: %s, height: %s'%(img.get_width(), img.get_height()))
    tile_width = int(img.get_width() * map_scale)
    tile_height = int(img.get_height() * map_scale)
    img = pygame.transform.scale(img, (tile_width, tile_height))
    surfs.append((x * tile_width, y * tile_height, img))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.VIDEORESIZE:
            WIDTH = e.w
            HEIGHT = e.h
            display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            for surf in surfs:
                display.blit(surf[2], (surf[0], surf[1]))
    pygame.display.update()


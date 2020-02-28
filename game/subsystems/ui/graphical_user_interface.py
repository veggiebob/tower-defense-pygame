from game.subsystems.ui.layout.layoutmanager import LayoutManager
from ..ui.ui_handler import ElementsHandler
from ..ui.layout.layout import Layout
import pygame
class GUI:
    def __init__(self, elements_handler: ElementsHandler, layout_manager: LayoutManager): # todo: this needs to take in a layout to work correctly
        self.elements_handler = elements_handler
        self.layout_manager = layout_manager
        self.needs_resize = True
    def update (self, mouse_position, mouse_down, mouse_press):
        if self.needs_resize:
            print('repositioned')
            print('current layout: %s'%self.layout_manager.getLayout())
            self.elements_handler.reposition_elements(self.layout_manager.getLayout())
            self.needs_resize = False
        self.elements_handler.update(mouse_position, mouse_down, mouse_press)
    def draw_to_surface (self, surface: pygame.Surface, draw_panel_borders=False) -> None:
        elements = self.elements_handler.get_elements()
        for e in elements:
            e.draw_on_surface(surface)

        if draw_panel_borders:
            panels = self.elements_handler.get_panels()
            for p in panels:
                pygame.draw.rect(surface, (255, 255, 255), (p.x, p.y, p.width, p.height), 2)

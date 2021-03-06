from game.subsystems.ui.elements.ui_elements import UiElement
from game.subsystems.ui.layout.layoutmanager import LayoutManager
from game.subsystems.ui.layout.panel import Panel
from ..ui.ui_handler import ElementsHandler
from ..ui.layout.layout import Layout
import pygame


class GUI:
    def __init__(self, layout_manager: LayoutManager):
        self.layout_manager = layout_manager
        self.needs_resize = True
        self.current_layout = layout_manager.getLayout()

    def get_elements_handler(self, name: str = None) -> ElementsHandler:
        if name is None: name = self.layout_manager.getCurrentLayoutName()
        return self.layout_manager.getElementHandler(name)

    def get_element(self, name: str) -> UiElement:
        return self.get_elements_handler().get_element(name)

    def get_panel(self, name: str) -> Panel:
        return self.layout_manager.getLayout().getPanel(name)

    def change_layout(self, layout_name: str):
        self.layout_manager.setCurrentLayout(layout_name)
        self.needs_resize = True

    def update(self, mouse_position, mouse_down, mouse_press):
        if self.needs_resize:
            self.get_elements_handler().reposition_elements(self.current_layout)
            self.needs_resize = False
        self.get_elements_handler().update(mouse_position, mouse_down, mouse_press)

    def draw_to_surface(self, surface: pygame.Surface, draw_panel_borders=False) -> None:
        elements = self.get_elements_handler().get_elements()
        # print('elements are %s'%', '.join(str(e) for e in elements))
        for e in elements:
            e.draw_on_surface(surface)

        if draw_panel_borders:
            panels = self.get_elements_handler().get_panels()
            for p in panels:
                pygame.draw.rect(surface, (255, 255, 255), (p.x, p.y, p.width, p.height), 2)

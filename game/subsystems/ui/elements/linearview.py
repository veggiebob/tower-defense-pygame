import random

import pygame

from game.subsystems.ui.elements.buttons import Button
from game.subsystems.ui.elements.ui_elements import UiElement, Vector


class LinearView(UiElement):#Linear layout for buttons
    REQ_ATTRS = ['elements', 'vertical'] + UiElement.REQ_ATTRS
    TYPE_ATTRS = {k[0]: k[1] for k in (list(UiElement.TYPE_ATTRS.items()) + list({
        'elements': [Button],
        'vertical': bool
    }.items()))}
    DEFAULT_ATTRS = {
        'vertical': True
    }
    def __init__(self):
        UiElement.__init__(self)
        self.vertical = True
        self.elements = [] # just so it doesn't get mad at me
    def draw(self) -> pygame.Surface:
        surf = pygame.Surface(self.size.to_tuple())
        i = -1
        num = len(self.elements)
        by = self.size.y/num
        for e in self.elements:
            i += 1
            surf.blit(e.draw(), (0, int(by*i)))
            e.position = self.position + Vector(0, by * i)
            e.size = Vector(self.size.x, by)
        return surf
    def draw_on_surface(self, surface: pygame.Surface) -> None:
        surface.blit(self.draw(), self.position.to_tuple())
    def update(self, mouse_position: Vector, mouse_down: bool, mouse_pressed: bool=None) -> None:
        UiElement.update(self, mouse_position, mouse_down, mouse_pressed)
        for e in self.elements:
            v: Button = e
            v.update(mouse_position, mouse_down, mouse_pressed)
    def get_elements (self) -> list:
        return self.elements
    def get_element_by_index (self, index: int) -> Button:
        return self.elements[index]
    def get_element_by_name (self, name: str) -> Button:
        for e in self.elements:
            if e.name == name:
                return e
        print('element not found!!!!!!!!!!!!')
        return None
    def add_element (self, element:Button):
        self.elements.append(element)
    def __str__ (self):
        return 'LinearView -> [%s]'%', '.join(str(e) for e in self.elements)
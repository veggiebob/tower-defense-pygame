from game.subsystems.ui.elements.ui_elements import UiElement, Vector
from game.common.text import Text
import pygame

class TextView(UiElement):
    REQ_ATTRS = ['text'] + UiElement.REQ_ATTRS
    TYPE_ATTRS = {k[0]:k[1] for k in (list(UiElement.TYPE_ATTRS.items()) + list({
        'text': str
    }.items()))} # adding two dictionaries together
    def __init__(self, position=Vector(), size=Vector(), text=Vector(), tint=(1,1,1)):
        UiElement.__init__(self, position, size, tint)
        self.text = text
    def draw(self) -> pygame.Surface:
        surf = pygame.Surface(self.size.to_tuple())
        pygame.draw.rect(surf, self.get_color().to_tuple(), (0, 0) + self.size.to_tuple(), 0)
        Text.DEFAULT_TEXT.draw_to_surface(surf, self.get_center().to_tuple(), self.text, 10, (0, 0, 0))
        return surf
    def draw_on_surface(self, surface: pygame.Surface) -> None:
        surface.blit(self.draw(), self.position.to_tuple())

class Button(TextView): # inheritance gang
    REQ_ATTRS = TextView.REQ_ATTRS
    TYPE_ATTRS = TextView.TYPE_ATTRS
    def __init__(self, position=Vector(), size=Vector(), text="", tint=(1,1,1)):
        TextView.__init__(self, position, size, text, tint)

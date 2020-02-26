from game.subsystems.ui.elements.ui_elements import *
from game.common.text import Text

class Button(UiElement):
    def __init__(self, position, size, text="", tint=(1,1,1)):
        UiElement.__init__(self, position, size, tint)
        self.text = text

    def draw(self) -> pygame.Surface:
        surf = pygame.Surface((self.size.x, self.size.y))
        ac = self.get_color()
        pc = self.get_color()
        surf.fill(ac)
        pygame.draw.rect(surf, pc, (0, 0, self.size.x, self.size.y), 1)
        Text.DEFAULT_TEXT.draw_to_surface(surf, [self.size.x / 2, self.size.y / 2], self.text, 10, (0, 0, 0))
        return surf

    def draw_on_surface(self, surface):
        surface.blit(self.draw(), self.position.to_tuple())

class TextView(UiElement):
    def __init__(self, position, size, text, tint=(1,1,1)):
        UiElement.__init__(self, position, size, tint)
        self.text = text
    def draw(self) -> pygame.Surface:
        surf = pygame.Surface(self.size.to_tuple())
        ac = self.get_color()
        Text.DEFAULT_TEXT.draw_to_surface(surf, self.get_center().to_tuple(), self.text, 10, (0, 0, 0))
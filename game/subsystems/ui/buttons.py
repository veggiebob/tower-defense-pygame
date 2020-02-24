from game.subsystems.ui.ui_elements import *
from game.common.text import DEFAULT_TEXT

class Button(UiElement):
    def __init__(self, position, size, text="", color=(200, 200, 200)):
        UiElement.__init__(self, position, size)
        self.text = text
        self.color = color
        self.dark_color = (color[0] / 2, color[1] / 2, color[2] / 2)
        self.super_dark_color = (self.dark_color[0] / 2, self.dark_color[1] / 2, self.dark_color[2] / 2)

    def set_cursor(self, c):
        cur = self.get_cursor()
        if cur is not None:
            c = cur
        return c

    def draw(self, tint=(1,1,1)) -> pygame.Surface:
        surf = pygame.Surface((self.size.x, self.size.y))
        ac = self.get_color()
        pc = self.get_color()
        ac = (tint[0] * ac[0], tint[1] * ac[1], tint[2] * ac[2])
        pc = (pc[0] * tint[0], pc[1] * tint[1], pc[2] * tint[2])
        surf.fill(ac)
        pygame.draw.rect(surf, pc, (0, 0, self.size.x, self.size.y), 1)
        DEFAULT_TEXT.draw_to_surface(surf, [self.size.x / 2, self.size.y / 2], self.text, 10, (0, 0, 0))
        return surf

    def draw_on_surface(self, surface):
        # pygame.draw.rect(surface, self.get_color(), self.position.to_tuple() + self.size.to_tuple(), 0)
        # pygame.draw.rect(surface, self.get_passive_color(), self.position.to_tuple() + self.size.to_tuple(), 1)
        # self.T.draw_to_surface(surface, (self.position + self.size * 0.5).to_tuple(), self.text, 10, (0, 0, 0))
        surface.blit(self.draw(), self.position.to_tuple())

    def resize(self, current_width, current_height, new_width, new_height):
        t = Transform(Vector(), Vector(new_width, new_height) / Vector(current_width, current_height))
        self.position = t.transform_vector(self.position)
        self.size = t.transform_vector(self.size)
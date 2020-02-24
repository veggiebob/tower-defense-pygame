import pygame, math
class Text:
    def __init__ (self, font_path:str=""):
        self.font_path = 'verdana.ttf' if font_path == "" else font_path
        try:
            self.font = pygame.font.Font(self.font_path, 20)
        except:
            raise Exception("please put in a valid font path")
        self.fonts = {
            20:self.font
        }
    def draw (self, txt="sample text", size=20, color=(0,0,0)):
        size = int(size)
        try:
            self.fonts[size]
        except:
            self.fonts[size] = pygame.font.Font(self.font_path, size)

        fo = self.fonts[size]
        surf = fo.render(str(txt), True, color)
        return surf
    def draw_to_surface (self, surface, position, txt="sample text", size=20, color=(0,0,0)):
        surf = self.draw(txt, size, color)
        surface.blit(surf, (int(position[0]-surf.get_width()/2), int(position[1]-surf.get_height()/2)))
    
    def get_text_size (self, width, height, text_length):
        return min(width * 0.7 / math.sqrt(text_length), height / text_length) # todo: this will need to be tested

DEFAULT_TEXT = Text()
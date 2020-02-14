import pygame

class Orientation:
    VERTICAL = 0
    HORIZONTAL = 1
class Order:
    STANDARD = 0 # left to right / top to bottom
    REVERSED = 1 # right to left / bottom to top

class Panel:
    REQ_ATTRS = ['x', 'y', 'width', 'height']
    DEFAULT_ATTRS = {
        'inner_panels': [],
        'orientation': 'vertical'
    }
    # panels are on a 1x1 "view-window" in which they can be scaled back using these fractions
    def __init__ (self, x=None, y=None, w=None, h=None, name=None):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.name = name
    @staticmethod
    def from_rect (window, name):
        return Panel(window[0], window[1], window[2], window[3], name)
    def to_window (self, x, y, window_width, window_height):
        return Panel.from_rect(
            pygame.Rect(x + self.x * window_width, y + self.y * window_height, self.width * window_width, self.height * window_height),
            self.name
        )
    def to_rect (self, rect):
        return self.to_window(rect[0], rect[1], rect[2], rect[3])
    def get_rect (self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    def split (self, orientation, order, percentage, new_name): # returns a 2-length array of Panels
        if orientation == Orientation.VERTICAL:
            p = [
                Panel(self.x, self.y, self.width, self.height * percentage, self.name),
                Panel(self.x, self.y + self.height * percentage, self.width, self.height * (1-percentage), new_name)
            ]
        elif orientation == Orientation.HORIZONTAL:
            p = [
                Panel(self.x, self.y, self.width * percentage, self.height, self.name),
                Panel(self.x + self.width * percentage, self.y, self.width * (1-percentage), self.height, new_name)
            ]
        else:
            p = [None, None]
            print('you suck')

        if order == Order.REVERSED:
            return [p[1], p[0]]
        elif order == Order.STANDARD:
            return p
        else:
            print('you suck')
            return p
    def split_multiple (self, orientation, number, names=None):
        vertical = orientation == Orientation.VERTICAL
        plist = []
        b = self.width / number if not vertical else self.height / number
        if names is None or len(names) < number:
            names = ["%s_%d"%(self.name, i) for i in range(0, number)]
        for i in range(0, number):
            v = i/number
            if vertical:
                plist.append(Panel(self.x, self.y + b * i, self.width, b, names[i]))
            else:
                plist.append(Panel(self.x + b * i, self.y, b, self.height, names[i]))

        return plist
    def has_inner_panels (self):
        return hasattr(self, 'inner_panels')
    @staticmethod
    def listify_tree (self, transform=Transform()):
        if self.has_inner_panels():
            trans = Transform(transform.position + Vector())
            l = []
            for p in self.inner_panels:
                l.append(Panel.listify_tree(p))

    def get_all_inner (self):
        ps = [] # all the panels
        if self.has_inner_panels:

        else:
            return [self]
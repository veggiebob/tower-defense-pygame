import pygame

from game.common.math import Transform, Vector


class Orientation:
    VERTICAL = 0
    HORIZONTAL = 1
class Order:
    STANDARD = 0 # left to right / top to bottom
    REVERSED = 1 # right to left / bottom to top

class Panel:
    REQ_ATTRS = ['x', 'y', 'width', 'height']
    DEFAULT_ATTRS = {
        'orientation': 'vertical'
    }
    # panels are on a 1x1 "view-window" in which they can be scaled back using these fractions
    def __init__ (self, x=None, y=None, w=None, h=None, name=None):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.name = name
    def __str__ (self):
        return 'Panel %s -> (%s, %s), (%s, %s)'%(self.name, self.x, self.y, self.width, self.height) + (
            ' and has %d inner panels'%len(self.inner_panels) if self.has_inner_panels() else ''
        )
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
    def parse_tree (self: 'Panel', transform=Transform()):
        if self.has_inner_panels():
            # print('panel has attributes %s, %s, %s, %s'%(self.x, self.y, self.width, self.height))
            trans = Transform(transform.translation + Vector(self.x, self.y), transform.scale * Vector(self.width, self.height))
            l = [Panel.parse_tree(p, trans) for p in self.inner_panels]
            return l
        else:
            p = self
            pos = Vector(p.x, p.y)
            size = Vector(p.width, p.height)
            pos = transform.transform_vector(pos)
            size *= transform.scale
            p.x = pos.x
            p.y = pos.y
            p.width = size.x
            p.height = size.y
            return p

    @staticmethod
    def flatten_list_tree (self, panel_list=[]): # turns a list tree into an unordered, 1-D list
        if type(self) == list:
            for p in self:
                l = Panel.flatten_list_tree(p, panel_list)
                if type(l) != list:
                    panel_list.append(l)
            return panel_list
        else:
            return self


    def get_all_inner (self):
        ps = Panel.parse_tree(self)
        ps = Panel.flatten_list_tree(ps)
        return ps

    def get_layout (self):
        L = Layout()
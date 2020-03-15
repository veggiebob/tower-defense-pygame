from game.subsystems.ui.layout.layout import Layout
from game.subsystems.ui.ui_handler import ElementsHandler


class LayoutManager:
    def __init__ (self):
        self.layouts = {}
        self.element_handlers = {}
        self.current_layout_name = ""

    def getCurrentLayoutName(self):
        return self.current_layout_name

    def makeLayout (self, name):
        self.layouts[name] = Layout(name)
        self.element_handlers[name] = []

    def getLayout (self, name=None) -> Layout:
        if name is None:
            name = self.current_layout_name
        try:
            return self.layouts[name]
        except:
            raise Exception('LayoutManager could not get layout %s'%name)
    def getElementHandler (self, name=None) -> ElementsHandler:
        if name is None:
            name = self.current_layout_name
        try:
            return self.element_handlers[name]
        except:
            print('tried to get layout %s from %s'%(name, self.element_handlers))
            raise Exception('LayoutManager could not get element handler %s'%name)

    def setCurrentLayout (self, name):
        self.current_layout_name = name

    def addLayout (self, layout: Layout, element_handler: ElementsHandler, name=None, set_current=False):
        if name is None:
            name = layout.name
        self.layouts[name] = layout
        self.element_handlers[name] = element_handler
        print('adding layout and element handler %s'%name)
        if set_current:
            self.setCurrentLayout(name)

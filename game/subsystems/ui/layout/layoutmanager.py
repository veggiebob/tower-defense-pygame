from game.subsystems.ui.layout.layout import Layout


class LayoutManager:
    def __init__ (self):
        self.layouts = {}
        self.current_layout = ""

    def makeLayout (self, name):
        self.layouts[name] = Layout(name)

    def getLayout (self, name=None):
        if name is None:
            name = self.current_layout
        try:
            return self.layouts[name]
        except:
            return None

    def setCurrentLayout (self, name):
        self.current_layout = name
        if not name in self.layouts.keys():
            raise Exception("%s is not a layout name. The layout names are: %s"%(name, '[' + ', '.join(self.layouts.keys()) + ']'))

    def addLayout (self, layout: Layout, name=None):
        if name is None:
            name = layout.name
        self.layouts[name] = layout
        # if set_current:
        #     self.setCurrentLayout(name) # cannot set_current because you need the gui to change layouts properly

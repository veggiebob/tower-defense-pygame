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

    def addLayout (self, layout: Layout, name=None, set_current=False):
        if name is None:
            name = layout.name
        self.layouts[name] = layout
        if set_current:
            self.setCurrentLayout(name)

from game.subsystems.ui.layout.panel import Panel

class Layout:
    def __init__ (self, name="main_panel", intended_window=(0, 0, 1, 1)):
        self.name = name
        self.intended_window = intended_window
        self.panels = [Panel.from_rect(intended_window, name)]
    def getPanelId (self, name):
        index = 0
        for p in self.panels:
            if name == p.name:
                return index
            index += 1
        return -1
    def getPanel (self, name):
        return self.panels[self.getPanelId(name)]
    def getPanelsOnRect (self, rect):
        return [p.to_rect(rect) for p in self.panels]
    def splitPanel (self, name, orientation, order, percentage, new_name):
        new_panels = self.getPanel(name).split(orientation, order, percentage, new_name)
        self.panels.remove(self.getPanel(name))
        self.panels.append(new_panels[0])
        self.panels.append(new_panels[1])
    def splitPanelMultiple (self, panel_name, orientation, number, new_names=None):
        new_panels = self.getPanel(panel_name).split_multiple(orientation, number, new_names)
        self.panels.remove(self.getPanel(panel_name))
        for p in new_panels:
            self.panels.append(p)

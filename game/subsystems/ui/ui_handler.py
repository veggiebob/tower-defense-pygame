class ElementsHandler:
    @staticmethod
    def from_panel_list (panels:list) -> 'ElementsHandler':
        elements = []
        for p in panels:
            try:
                elements.append(p.ui_button)
            except: pass
            try:
                elements.append(p.ui_text)
            except: pass
        return ElementsHandler(panels, elements)

    def __init__ (self, panels: list, ui_elements: list):
        self.panels = panels
        self.elements = ui_elements
        self.keyed = False
        self.panel_keys = {}
        self.element_keys = {}
        self.do_key()

    def reposition_elements(self):
        for e in self.elements:
            e.position_on_panel(self.get_panel(e.panel_name))

    def update(self, mouse_position: bool, mouse_down: bool, mouse_pressed: bool):
        for e in self.elements:
            e.update(mouse_position, mouse_down, mouse_pressed)

    def do_key (self):
        for p in self.panels:
            self.panel_keys[p.name] = p
        for e in self.elements:
            self.element_keys[e.name] = e
        self.keyed = True

    def re_key (self):
        self.keyed = False
        self.do_key()

    def get_panel (self, name: str):
        if not self.keyed:
            self.do_key()
        return self.panel_keys[name]
    def get_element (self, name: str):
        if not self.keyed:
            self.do_key()
        return self.element_keys[name]
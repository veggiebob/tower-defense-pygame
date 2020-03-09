from game.subsystems.ui.graphical_user_interface import GUI

from game.common.math import Vector


class GamePlayer:
    def __init__ (self, game_state: GameState, gui: GUI): # todo: import GameState
        self.game_state = game_state
        self.gui = gui

    def set_on_click_for_element (self, name: str, onclick) -> None: # to be used in main
        self.gui.get_element(name).set_on_click_listener(onclick)

    def set_on_click_args_for_element (self, name: str, args: dict) -> None: # to be used in main
        self.gui.get_element(name).set_click_args(args)

    def set_element_click (self, name: str, onclick, args: dict) -> None:
        self.set_on_click_for_element(name, onclick)
        self.set_on_click_args_for_element(name, args)

    def update (self, mouse_position: Vector, mouse_down: bool, mouse_pressed: bool):
        self.gui.update(mouse_position, mouse_down, mouse_pressed)
        self.game_state.update(mouse_position.to_tuple(), mouse_down, mouse_pressed) # todo: ui shouldn't handle game interaction
        # mouse_pressed is only true the instant the mouse is actually pressed down
        # mouse_down is true whenever the mouse is pressed down
        # mouse_position is the position, in pixels. Transform by environment . . . ?

    def draw_to_surface (self, surface):
        game_area_panel = self.gui.get_panel('game_area') # todo: make sure this works
        # todo: request a background of this width and height. Changes in size should be handled in art,
        #  and game state should be given a background of this dynamic size, essentially provided by Elijah's code
        #  or maybe just clip the surface in the game area
        background = self.game_state.get_background(game_area_panel.width, game_area_panel.height)
        surface.blit((int(game_area_panel.x), int(game_area_panel.y)), background)
        for e in self.game_state.get_enemies(): # todo: gets Enemy Surfaces with locations
            surface.blit(*e) # put it like ((x, y), surface)
        for t in self.game_state.get_towers(): # todo: gets Tower Surfaces with locations
            surface.blit(*t)
        self.gui.draw_to_surface(surface, True)

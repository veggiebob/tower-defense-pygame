from game.subsystems.ui.graphical_user_interface import GUI

from game.common.math import Vector


class GamePlayer:
    def __init__ (self, game_state: GameState, gui: GUI): # todo: import GameState
        self.game_state = game_state
        self.gui = gui
        self.holding_tower = False
        self.held_tower = None # tower that is being dragged around by the mouse

    def update (self, mouse_position: Vector, mouse_down: bool, mouse_pressed: bool):
        self.gui.update(mouse_position, mouse_down, mouse_pressed)

    def draw_to_surface (self, surface):
        game_area_panel = self.gui.
        surface.blit()
        self.gui.draw_to_surface(surface, True)

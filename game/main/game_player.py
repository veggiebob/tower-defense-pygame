from game.subsystems. # todo: import GameState

from game.common.math import Vector


class GamePlayer:
    def __init__ (self, game_state: GameState, gui: GUI):
        self.game_state = game_state
        self.gui = gui

    def update (self, mouse_position: Vector, mouse_delta: float):

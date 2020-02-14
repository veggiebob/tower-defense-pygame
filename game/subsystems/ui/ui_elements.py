import abc, pygame
from game.common.math import *

cursors = {
    'default': pygame.cursors.arrow,
    'hand': pygame.cursors.diamond,
    'press': pygame.cursors.broken_x
}


class MouseButton:
    RIGHT = 3
    LEFT = 1
    MIDDLE = 2


class ColorState:
    # yaml
    DEFAULT_ATTRS = {
        'off': (200, 200, 200),
        'hovering': (100, 100, 100),
        'active': (200, 150, 150)
    }

    def __init__(self, off, hovering, active):
        self.off = off
        self.hovering = hovering
        self.active = active

    # if not defined, set these
    def may_set_defaults(self):
        if self.off is None: self.off = ColorState.DEFAULT_ATTRS.OFF
        if self.hovering is None: self.hovering = ColorState.DEFAULT_ATTRS['HOVERING']
        if self.active is None: self.active = ColorState.DEFAULT_ATTRS['ACTIVE']

    # force set to default
    def set_defaults(self):
        self.off = None
        self.hovering = None
        self.active = None
        self.may_set_defaults()


class UiEvent:
    HOVER = 'hover'
    ACTIVE = 'active'
    MOVE = 'move'
    HOVER_ON = 'hover_on'
    HOVER_OFF = 'hover_off'
    ACTIVE_ON = 'active_on'
    ACTIVE_OFF = 'active_off'
    CHANGE = 'change'

    def __init__(self, **kwargs):
        self.properties = {}
        for k, v in kwargs.items():
            self.properties[k] = v

    def has(self, property):
        try:
            return self.properties[property]
        except:
            return False

    def put(self, key, value=True):
        self.properties[key] = value

    def from_state(self, past_state):  # handles on-off states
        # hovering
        if self.has(UiEvent.HOVER):
            if not past_state.has(UiEvent.HOVER):
                self.put(UiEvent.HOVER_ON)
        else:
            if past_state.has(UiEvent.HOVER):
                self.put(UiEvent.HOVER_OFF)
        # activity
        if self.has(UiEvent.ACTIVE):
            if not past_state.has(UiEvent.ACTIVE):
                self.put(UiEvent.ACTIVE_ON)
        else:
            if past_state.has(UiEvent.ACTIVE):
                self.put(UiEvent.ACTIVE_OFF)


class UiElement(abc.ABC):  # make it an abstract class
    @abc.abstractmethod
    def draw_on_surface(self): pass

    @abc.abstractmethod
    def update(self, mouse_position: Vector, mouse_down: bool): pass

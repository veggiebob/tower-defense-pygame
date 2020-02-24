import abc, pygame
from game.common.math import *

class Cursor:
    DEFAULT = pygame.cursors.arrow
    HAND = pygame.cursors.diamond
    PRESS = pygame.cursors.broken_x


class MouseButton:
    RIGHT = 3
    LEFT = 1
    MIDDLE = 2


class ColorState:
    # yaml
    DEFAULT_ATTRS = {
        'OFF': (200, 200, 200),
        'HOVERING': (100, 100, 100),
        'ACTIVE': (200, 150, 150)
    }

    def __init__(self, off, hovering, active):
        self.off = off
        self.hovering = hovering
        self.active = active

    # if not defined, set these
    def may_set_defaults(self):
        if self.off is None: self.off = ColorState.DEFAULT_ATTRS['OFF']
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
    CLICKED = 'clicked'
    CHANGE = 'change'

    def __init__(self, **kwargs):
        self.properties = {}
        for k, v in kwargs.items():
            self.properties[k] = v

    def has(self, _property: str) -> bool:
        try:
            return self.properties[_property]
        except:
            return False

    def put(self, key: str, value=True) -> None:
        self.properties[key] = value

    def from_state(self, past_state: 'UiEvent') -> None:  # handles on-off states
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
    def __init__ (self, position: Vector, size: Vector):
        self.position = position
        self.size = size
        self.on_click_listener = None
        self.state = UiEvent()
        self.state_colors = {
            UiEvent.ACTIVE: (100, 100, 100),
            UiEvent.HOVER: (150, 150, 150),
            UiEvent.CLICKED: (0, 0, 0),
            'default': (255, 255, 255)
        }
        self.state_cursors = {
            UiEvent.ACTIVE: Cursor.PRESS,
            UiEvent.HOVER: Cursor.HAND,
            'default': Cursor.DEFAULT
        }

    @abc.abstractmethod
    def draw (self) -> pygame.Surface: pass

    @abc.abstractmethod
    def draw_on_surface(self, surface: pygame.Surface): pass

    def set_color (self, event_name: str, color):
        self.state_colors[event_name] = color

    def set_state_colors (self, events_colors: dict):
        self.state_colors = events_colors

    def get_color (self):
        for k,v in self.state_colors.items():
            if self.check_state(k):
                return v

    def get_cursor (self):
        for k,v in self.state_cursors.items():
            if self.check_state(k):
                return v

    def check_state (self, _property: str):
        return self.state.has(_property)

    def update(self, mouse_position: Vector, mouse_down: bool, mouse_pressed: bool=None) -> None:
        new_event = UiEvent()
        if mouse_position.in_box(self.position, self.size):
            new_event.put(UiEvent.HOVER)
            if mouse_down:
                new_event.put(UiEvent.ACTIVE)
            if mouse_pressed:
                new_event.put(UiEvent.CLICKED)
        new_event.from_state(self.state)
        self.state = new_event
        if self.check_state(UiEvent.CLICKED):
            self.click()

    def get_center (self) -> Vector:
        return self.position + self.size * 0.5

    def click (self):
        if self.on_click_listener is not None:
            self.on_click_listener()

    def set_on_click_listener (self, listener):
        self.on_click_listener = listener


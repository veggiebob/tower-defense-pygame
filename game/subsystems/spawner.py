from collections import Callable


class Spawner:
    def __init__ (self, out_callback:Callable = None, spawn_ticks:int=10):
        self.callback = out_callback
        self.items = []
        self.ticks = 0
        self.spawn_ticks = spawn_ticks
    def add_item (self, item):
        self.items.append(item)
    def output_item (self) -> object:
        out = self.items.pop(0)
        if self.callback is not None:
            self.callback(out)
        return out
    def empty (self) -> bool:
        return len(self.items) == 0
    def reset (self):
        self.ticks = self.spawn_ticks
    def tick (self):
        if self.empty():
            self.reset()
        else:
            self.ticks -= 1
            if self.ticks < 0:
                self.output_item()
                self.reset()
    def flush (self):
        self.items = []
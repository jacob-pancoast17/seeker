import constants as c
from object import Object
import time

class Hostile(Object):
    '''
    Constructor creates a hostile object which "is-an" object

    param: 
        same as object parameters
    returns:
        nothing
    '''
    def __init__(self, size, x, y, color):
        super().__init__(size, x, y, color)

    def move(self):
        if self.obj.center_y < 0:
            self.obj.center_y = c.WINDOW_HEIGHT - (c.TILE_HEIGHT / 2) - 5
        else:
            self.obj.center_y -= c.VELOCITY_MULTIPLIER

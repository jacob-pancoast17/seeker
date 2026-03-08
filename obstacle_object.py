import arcade
import constants as c
from object import Object

class Obstacle(arcade.SpriteSolidColor):
    '''
    Constructor creates a obstacle object which "is-an" object

    param: 
        same as object parameters
    returns:
        nothing
    '''
    def __init__ (self, size, row, column, color):
        super().__init__(width = size,
            height = size,
            color = color)
        
        self.center_x = (c.MARGIN + c.TILE_WIDTH) * row + c.MARGIN + c.TILE_WIDTH // 2
        self.center_y = (c.MARGIN + c.TILE_HEIGHT) * column + c.MARGIN + c.TILE_HEIGHT // 2
        self.angle = 0
    
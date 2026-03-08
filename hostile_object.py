import arcade
import constants as c
from game_over_screen import GameOver
from object import Object
import time

class Hostile(arcade.SpriteSolidColor):
    '''
    Constructor creates a hostile object which "is-an" object

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

    def try_move(self, window, player):
        if self.center_y < 0:
            temp = self.center_y
            self.center_y = c.WINDOW_HEIGHT - (c.TILE_HEIGHT / 2) - 5
            hit_list = arcade.check_for_collision(
                self, 
                player)
            if hit_list:
                window.show_view(GameOver())
                return False
            self.center_y = temp
        else:
            self.center_y -= c.VELOCITY_MULTIPLIER
            hit_list = arcade.check_for_collision(
                self, 
                player)
            if hit_list:
                window.show_view(GameOver())
                return False
            self.center_y += c.VELOCITY_MULTIPLIER
        return True


    def move(self):
        if self.center_y < 0:
            self.center_y = c.WINDOW_HEIGHT - (c.TILE_HEIGHT / 2) - 5
        else:
            self.center_y -= c.VELOCITY_MULTIPLIER

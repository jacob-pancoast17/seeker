import arcade
import constants as c
from game_over_screen import GameOver
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

    def try_move(self, window, player):
        if self.obj.center_y < 0:
            temp = self.obj.center_y
            self.obj.center_y = c.WINDOW_HEIGHT - (c.TILE_HEIGHT / 2) - 5
            hit_list = arcade.check_for_collision(
                self.to_sprite(), 
                player)
            if hit_list:
                window.show_view(GameOver())
                return False
            self.obj.center_y = temp
        else:
            self.obj.center_y -= c.VELOCITY_MULTIPLIER
            hit_list = arcade.check_for_collision(
                self.to_sprite(), 
                player)
            if hit_list:
                window.show_view(GameOver())
                return False
            self.obj.center_y += c.VELOCITY_MULTIPLIER
        return True


    def move(self):
        if self.obj.center_y < 0:
            self.obj.center_y = c.WINDOW_HEIGHT - (c.TILE_HEIGHT / 2) - 5
        else:
            self.obj.center_y -= c.VELOCITY_MULTIPLIER

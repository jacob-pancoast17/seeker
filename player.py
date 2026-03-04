import arcade
import constants as c

class Player():
    def __init__(self, size, row, column, color):
        # For now just makes cubes
        # Right now this also ignores the angle parameter
        self.obj = arcade.SpriteSolidColor(
            width = size,
            height = size,
            center_x = (c.MARGIN + c.TILE_WIDTH) * row + c.MARGIN + c.TILE_WIDTH // 2,
            center_y = (c.MARGIN + c.TILE_HEIGHT) * column + c.MARGIN + c.TILE_HEIGHT // 2,
            color = color,
            angle = 0
        )

        self.curr_x = row
        self.curr_y = column

    def get_curr_x(self):
        return self.curr_x
    
    def get_curr_y(self):
        return self.curr_y
    
    def move(self, key):

        if (key == arcade.key.UP and
            self.curr_y < c.ROW_COUNT - 1):
            #print("UP")
            self.obj.center_y += c.VELOCITY_MULTIPLIER
            self.curr_y += 1

        elif (key == arcade.key.DOWN and
              self.curr_y > 0):
            #print("DOWN")
            self.obj.center_y -= c.VELOCITY_MULTIPLIER
            self.curr_y -= 1

        elif (key == arcade.key.LEFT and
              self.curr_x > 0):
            #print("LEFT")
            self.obj.center_x -= c.VELOCITY_MULTIPLIER
            self.curr_x -= 1

        elif (key == arcade.key.RIGHT and
              self.curr_x < c.COLUMN_COUNT - 1):
            #print("RIGHT")
            self.obj.center_x += c.VELOCITY_MULTIPLIER
            self.curr_x += 1

        print(f"[{self.curr_x}, {self.curr_y}]")

    def to_sprite(self):
        return self.obj
import arcade
import constants as c

class Player():
    def __init__(self, row, column):
        # For now just makes cubes
        # Right now this also ignores the angle parameter

        '''
        self.obj = arcade.Sprite(
            path_or_texture= "sprites/bear.png",
            scale = 1.0,
            center_x = (c.MARGIN + c.TILE_WIDTH) * row + c.MARGIN + c.TILE_WIDTH // 2,
            center_y = (c.MARGIN + c.TILE_HEIGHT) * column + c.MARGIN + c.TILE_HEIGHT // 2,
            angle = 180.0
        )
        '''
        # program is broken without this so I just commented out the code 
        # above to use later when we have the bear.png
        self.obj = arcade.SpriteSolidColor(
            width = c.TILE_WIDTH,
            height = c.TILE_HEIGHT,
            center_x = (c.MARGIN + c.TILE_WIDTH) * row + c.MARGIN + c.TILE_WIDTH // 2,
            center_y = (c.MARGIN + c.TILE_HEIGHT) * column + c.MARGIN + c.TILE_HEIGHT // 2,
            color = arcade.color.GREEN
        )

        self.curr_x = row
        self.curr_y = column

    def get_curr_x(self):
        return self.curr_x
    
    def get_curr_y(self):
        return self.curr_y
    
    def try_move(self, key, object_type, objects_sprite_list):
        
        if key == arcade.key.UP:
            if self.curr_y >= c.ROW_COUNT - 1:
                return False
            
            elif (object_type == 'Obstacle' or
                  object_type == 'Hostile'):
                self.obj.center_y += c.VELOCITY_MULTIPLIER
                hit_list = arcade.check_for_collision_with_list(
                    self.obj,
                    objects_sprite_list
                )
                self.obj.center_y -= c.VELOCITY_MULTIPLIER
                if hit_list:
                    return False

            print("Good to go!")
                
            return True
        
        elif key == arcade.key.DOWN:
            if self.curr_y <= 0:
                return False
            
            elif (object_type == 'Obstacle' or
                  object_type == 'Hostile'):
                self.obj.center_y -= c.VELOCITY_MULTIPLIER
                hit_list = arcade.check_for_collision_with_list(
                    self.obj,
                    objects_sprite_list
                )
                self.obj.center_y += c.VELOCITY_MULTIPLIER
                if hit_list:
                    return False
            print("Good to go!")
                
            return True
        
        elif key == arcade.key.LEFT:
            if self.curr_x <= 0:
                return False
            
            elif (object_type == 'Obstacle' or
                  object_type == 'Hostile'):
                self.obj.center_x -= c.VELOCITY_MULTIPLIER
                hit_list = arcade.check_for_collision_with_list(
                    self.obj,
                    objects_sprite_list
                )
                self.obj.center_x += c.VELOCITY_MULTIPLIER
                if hit_list:
                    return False
            print("Good to go!")
                
            return True
        
        elif key == arcade.key.RIGHT:
            if self.curr_x >= c.COLUMN_COUNT - 1:
                return False
            
            elif (object_type == 'Obstacle' or
                  object_type == 'Hostile'):
                self.obj.center_x += c.VELOCITY_MULTIPLIER
                hit_list = arcade.check_for_collision_with_list(
                    self.obj,
                    objects_sprite_list
                )
                self.obj.center_x -= c.VELOCITY_MULTIPLIER
                if hit_list:
                    return False
            print("Good to go!")
                
            return True
    
    def move(self, key):

        if (key == arcade.key.UP and
            self.curr_y < c.ROW_COUNT - 1):
            #print("UP")
            self.obj.center_y += c.VELOCITY_MULTIPLIER
            self.curr_y += 1
            self.obj.change_angle = 180
            self.obj.angle = self.obj.change_angle

        elif (key == arcade.key.DOWN and
              self.curr_y > 0):
            #print("DOWN")
            self.obj.center_y -= c.VELOCITY_MULTIPLIER
            self.curr_y -= 1
            self.obj.change_angle = 0
            self.obj.angle = self.obj.change_angle

        elif (key == arcade.key.LEFT and
              self.curr_x > 0):
            #print("LEFT")
            self.obj.center_x -= c.VELOCITY_MULTIPLIER
            self.curr_x -= 1
            self.obj.change_angle = 90
            self.obj.angle = self.obj.change_angle

        elif (key == arcade.key.RIGHT and
              self.curr_x < c.COLUMN_COUNT - 1):
            #print("RIGHT")
            self.obj.center_x += c.VELOCITY_MULTIPLIER
            self.curr_x += 1
            self.obj.change_angle = 270
            self.obj.angle = self.obj.change_angle

        print(f"[{self.curr_x}, {self.curr_y}]")

    def to_sprite(self):
        return self.obj
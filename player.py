import arcade
import constants as c

class Player(arcade.SpriteSolidColor):
    def __init__(self, size, row, column, color):
        # For now just makes cubes
        # Right now this also ignores the angle parameter
        super().__init__(width = size,
            height = size,
            color = color)
        
        self.center_x = (c.MARGIN + c.TILE_WIDTH) * row + c.MARGIN + c.TILE_WIDTH // 2
        self.center_y = (c.MARGIN + c.TILE_HEIGHT) * column + c.MARGIN + c.TILE_HEIGHT // 2
        self.angle = 0
    
    def try_move(self, key, object_type, objects_sprite_list):
        
        if key == arcade.key.UP:
            
            if self.center_y >= c.WINDOW_HEIGHT - c.TILE_HEIGHT:
                return False
            
            elif (object_type == 'Obstacle' or
                  object_type == 'Hostile'):
                self.center_y += c.VELOCITY_MULTIPLIER
                hit_list = arcade.check_for_collision_with_list(
                    self,
                    objects_sprite_list
                )
                self.center_y -= c.VELOCITY_MULTIPLIER
                if hit_list:
                    return False

            print("Good to go!")
                
            return True
        
        elif key == arcade.key.DOWN:
            if self.center_y <= c.TILE_HEIGHT:
                return False
            
            elif (object_type == 'Obstacle' or
                  object_type == 'Hostile'):
                self.center_y -= c.VELOCITY_MULTIPLIER
                hit_list = arcade.check_for_collision_with_list(
                    self,
                    objects_sprite_list
                )
                self.center_y += c.VELOCITY_MULTIPLIER
                if hit_list:
                    return False
            print("Good to go!")
                
            return True
        
        elif key == arcade.key.LEFT:
            if self.center_x <= c.TILE_HEIGHT:
                return False
            
            elif (object_type == 'Obstacle' or
                  object_type == 'Hostile'):
                self.center_x -= c.VELOCITY_MULTIPLIER
                hit_list = arcade.check_for_collision_with_list(
                    self,
                    objects_sprite_list
                )
                self.center_x += c.VELOCITY_MULTIPLIER
                if hit_list:
                    return False
            print("Good to go!")
                
            return True
        
        elif key == arcade.key.RIGHT:
            if self.center_x >= c.WINDOW_WIDTH - c.TILE_HEIGHT:
                return False
            
            elif (object_type == 'Obstacle' or
                  object_type == 'Hostile'):
                self.center_x += c.VELOCITY_MULTIPLIER
                hit_list = arcade.check_for_collision_with_list(
                    self,
                    objects_sprite_list
                )
                self.center_x -= c.VELOCITY_MULTIPLIER
                if hit_list:
                    return False
            print("Good to go!")
                
            return True

            

    
    def move(self, key):

        if (key == arcade.key.UP and
            self.center_y < c.WINDOW_HEIGHT - c.TILE_HEIGHT):
            #print("UP")
            self.center_y += c.VELOCITY_MULTIPLIER

        elif (key == arcade.key.DOWN and
              self.center_y > c.TILE_HEIGHT):
            #print("DOWN")
            self.center_y -= c.VELOCITY_MULTIPLIER

        elif (key == arcade.key.LEFT and
              self.center_x > c.TILE_HEIGHT):
            #print("LEFT")
            print(self.center_x)
            self.center_x -= c.VELOCITY_MULTIPLIER

        elif (key == arcade.key.RIGHT and
              self.center_x < c.WINDOW_WIDTH - c.TILE_HEIGHT):
            #print("RIGHT")
            self.center_x += c.VELOCITY_MULTIPLIER

        print(f"[{self.center_x}, {self.center_y}]")
import arcade
import constants as c
from hostile_object import Hostile
from obstacle_object import Obstacle
from player import Player

'''
GameView represents a window object
'''
class GameView(arcade.View):
   
    def __init__(self):
        '''
        Constructor

        param: self
        return: nothing
        '''
        super().__init__()

        self.background_color = c.background

        # Timing
        self.world_time = 0
        self.next_move = 0

        self.grid = None
        self.obstacles_sprites = None
        self.hostiles_sprites = None
        self.hostiles_objs = None

        self.player_sprite = None
        self.player = None

        self.setup()

    def setup(self):
        '''
        setup is run whenever the window is initially created,
        and creates the grid, objects, and the player

        param: self
        return: nothing
        '''

        # Create grid
        self.grid = arcade.SpriteList()

        # Create obstacles
        self.obstacles_sprites = arcade.SpriteList()
        rock = Obstacle(c.TILE_SIZE, 3, 6, arcade.csscolor.DARK_SLATE_GRAY)
        self.obstacles_sprites.append(rock.to_sprite())

        # Create hostiles
        self.hostiles_sprites = arcade.SpriteList()
        car = Hostile(c.TILE_SIZE, 12, 6, arcade.csscolor.RED)
        self.hostiles_sprites.append(car.to_sprite())

        self.hostile_objs = []
        self.hostile_objs.append(car)

        # Create player object and "list" of players--
        # pyarcade can only drawing using a SpriteList, so
        # player has to be in a SpriteList
        self.player = Player(c.TILE_WIDTH,
                              c.STARTING_X,
                                c.STARTING_Y, 
                                color = arcade.color.GREEN)
        self.player_sprite = arcade.SpriteList()

        # Use the player class's to_sprite() to add the
        # SPRITE version to the SpriteList (to match types)
        self.player_sprite.append(self.player.to_sprite())

        # Create the grid
        for row in range(c.ROW_COUNT):

            for column in range(c.COLUMN_COUNT):

                # Append a new cell
                sprite = arcade.SpriteSolidColor(c.TILE_WIDTH,
                                                  c.TILE_HEIGHT,
                                                    color=arcade.color.WHITE)

                # Set the cell's center based on grid position
                sprite.center_x = (c.MARGIN + c.TILE_WIDTH) * column + c.MARGIN + c.TILE_WIDTH // 2
                sprite.center_y = (c.MARGIN + c.TILE_HEIGHT) * row + c.MARGIN + c.TILE_HEIGHT // 2

                # Append to list of all grid sprites to draw
                self.grid.append(sprite)

    def on_draw(self):
        """
        Render the screen.
        """
        # We should always start by clearing the window pixels
        self.clear()

        # Draw the shapes representing our current grid
        self.grid.draw()
        self.player_sprite.draw() # Draw the player on TOP of the grid
        self.obstacles_sprites.draw()
        self.hostiles_sprites.draw()
        
    def on_update(self, delta_time):
        '''
        Happens every frame
        '''
        self.world_time += delta_time
        speed = 1

        if self.world_time >= self.next_move:
            self.next_move += speed
            for hostile in self.hostile_objs:
                hostile.move()
    

    def on_key_press(self, key, modifiers):
        '''
        on_key_press detects when a key is pressed

        param: self
           symbol - key pressed
           modifiers - e.g. capslock or numlock
        '''

        # If the player presses a key, update the speed if able to move
        move = True
        if (key == arcade.key.UP or
            key == arcade.key.DOWN or
            key == arcade.key.LEFT or
            key == arcade.key.RIGHT):

            # Test if player is going to collide with something
            if not self.player.try_move(key, 'Obstacle', self.obstacles_sprites):
                move = False
            elif not self.player.try_move(key, 'Hostile', self.hostiles_sprites):
                from game_over_screen import GameOver
                self.window.show_view(GameOver())

            # If not, we are good to move!
            if move == True:
                self.player.move(key)

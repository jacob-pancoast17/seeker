import arcade
import constants as c
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

        self.grid = None
        self.obstacles = None

        self.player = None
        self.player_list = None

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
        # Create objects
        self.obstacles = arcade.SpriteList()
        rock = Obstacle(c.TILE_SIZE, 3, 6, arcade.csscolor.DARK_SLATE_GRAY)
        self.obstacles.append(rock.to_sprite())

        # Create player object and "list" of players--
        # pyarcade can only drawing using a SpriteList, so
        # player has to be in a SpriteList
        self.player = Player(c.TILE_WIDTH,
                              c.STARTING_X,
                                c.STARTING_Y, 
                                color = arcade.color.GREEN)
        self.player_list = arcade.SpriteList()

        # Use the player class's to_sprite() to add the
        # SPRITE version to the SpriteList (to match types)
        self.player_list.append(self.player.to_sprite())

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
        self.player_list.draw() # Draw the player on TOP of the grid
        self.obstacles.draw()
    

    def on_key_press(self, key, modifiers):
        '''
        on_key_press detects when a key is pressed

        param: self
           symbol - key pressed
           modifiers - e.g. capslock or numlock
        '''
        # If the player presses a key, update the speed
        if (key == arcade.key.UP or
            key == arcade.key.DOWN or
            key == arcade.key.LEFT or
            key == arcade.key.RIGHT):
            # Call Player's move function
            if self.player.try_move(key, 'Obstacle', self.obstacles):
                self.player.move(key)
        elif key == arcade.key.ESCAPE:
            from game_over_screen import GameOver
            self.window.show_view(GameOver())

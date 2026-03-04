import arcade
import constants as c
import game_over_screen as GameOver
from object import Object
from player import Player

'''
GameView represents a window object
'''
class GameView(arcade.View):
    '''
    Constructor

    param: arcade window
    return: nothing
    '''
    def __init__(self):
        super().__init__()

        self.background_color = c.background
        # self.shape_list = None
        # self.object_list = None
        self.grid = arcade.SpriteList()
        self.objects = arcade.SpriteList()
        self.grid_sprites = []
        self.player = Player(c.TILE_WIDTH, 0, 7, color = arcade.color.GREEN)
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player.to_sprite())

        # rock = Object(30 , 4, 4, arcade.color.BATTLESHIP_GREY)

        #self.curr_player_pos = [0, 7]
        # self.grid = []
        for row in range(c.ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid_sprites.append([])
            for column in range(c.COLUMN_COUNT):
                x = (c.MARGIN + c.TILE_WIDTH) * column + c.MARGIN + c.TILE_WIDTH // 2
                y = (c.MARGIN + c.TILE_HEIGHT) * row + c.MARGIN + c.TILE_HEIGHT // 2
                if(row == 0 and column == 7):
                    #sprite = player.to_sprite()
                    sprite = arcade.SpriteSolidColor(c.TILE_WIDTH, c.TILE_HEIGHT, color=arcade.color.WHITE)  # Append a cell
                elif(row == 4 and column == 4):
                    #sprite = arcade.SpriteSolidColor(c.TILE_WIDTH, c.TILE_HEIGHT, color=arcade.color.BATTLESHIP_GREY)
                    sprite = arcade.SpriteSolidColor(c.TILE_WIDTH, c.TILE_HEIGHT, color=arcade.color.WHITE)
                else:
                    sprite = arcade.SpriteSolidColor(c.TILE_WIDTH, c.TILE_HEIGHT, color=arcade.color.WHITE)  # Append a cell
                sprite.center_x = x
                sprite.center_y = y
                self.grid.append(sprite)
                self.grid_sprites[row].append(sprite)


        # Set the window's background color
        self.background_color = arcade.color.BLACK
        # Create shapes from the grid
        # self.recreate_grid()

    def recreate_grid(self):
        """
        Create the shapes for our current grid.


        We look at the values in each cell.
        If the cell contains 0 we create a white shape.
        If the cell contains 1 we create a green shape.
        """
        self.shape_list = arcade.shape_list.ShapeElementList()
        for row in range(c.ROW_COUNT):
            for column in range(c.COLUMN_COUNT):
                if self.grid[row][column] == 0:
                    color = arcade.color.WHITE
                # elif self.grid[row][column] == rock:
                #     color = arcade.color.BATTLESHIP_GREY
                else:
                    color = arcade.color.GREEN


                x = (c.MARGIN + c.TILE_WIDTH) * column + c.MARGIN + c.TILE_WIDTH // 2
                y = (c.MARGIN + c.TILE_HEIGHT) * row + c.MARGIN + c.TILE_HEIGHT // 2


                current_rect = arcade.shape_list.create_rectangle_filled(
                    x, y, c.TILE_WIDTH, c.TILE_HEIGHT, color,
                )
                self.shape_list.append(current_rect)


    def on_draw(self):
        """
        Render the screen.
        """
        # We should always start by clearing the window pixels
        self.clear()


        # Draw the shapes representing our current grid
        self.grid.draw()
        self.player_list.draw()
        

    '''
    on_key_press detects when a key is pressed

    param: self
           symbol - key pressed
           modifiers - e.g. capslock or numlock
    '''

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        # If the player presses a key, update the speed
        if (key == arcade.key.UP or
            key == arcade.key.DOWN or
            key == arcade.key.LEFT or
            key == arcade.key.RIGHT):
            self.player.move(key)
        elif key == arcade.key.ESCAPE:
            game_over = GameOver.GameOver()
            self.window.show_view(game_over)
        #self.grid_sprites[self.curr_player_pos[0]][self.curr_player_pos[1]] = 1
        # self.recreate_grid()

    '''
    run_window sets up the window and runs it

    param: self
    return: nothing
    '''
    def run_window(self):
        #self.setup()
        arcade.run()
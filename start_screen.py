import arcade
import arcade.gui
import constants as c
import game_view as GameView

'''
StartScreen represents the start screen view
'''
class StartScreen(arcade.View):
    '''
    Constructor calls arcade 'View' superclass constructor

    param: self
    return: nothing
    '''
    def __init__(self):
        super().__init__()

        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()

        play_texture = arcade.load_texture("sprites/play.png")
        play_button = arcade.gui.UITextureButton(
            width = 100,
            texture = play_texture
        )

        # Initialize button with on-click event
        @play_button.event("on_click")
        def on_click_play(event):
            print("Awesome!")
            game_view = GameView.GameView()
            self.window.show_view(game_view)

        self.anchor = self.uimanager.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x = "center_x",
            anchor_y = "center_y",
            child = play_button
        )

    '''
    on_show_view defines events that happen when switching
    to the start screen view

    param: self
    return: nothing
    '''
    def on_show_view(self):
        # Set background color
        self.window.background_color == c.start_screen_background

        # Reset view
        self.window.default_camera.use()
        self.uimanager.enable()

    '''
    on_hide_view defines events that happen when switching
    away from the start screen

    param: self
    return: nothing
    '''
    def on_hide_view(self):
        self.uimanager.disable()

    '''
    on_draw redraws the frame for the start screen

    param: self
    return: nothing
    '''
    def on_draw(self):
        # Reset window
        self.clear()

        # Draw UI elements
        self.uimanager.draw()
        
    
import os


class Settings():
    def __init__(self):
        # Initializing game settings.
        self.screen_width = 500
        self.screen_height = 900

        # Background settings
        self.bg_color = (230, 230, 230)
        # os.path.join() for cross-platforming
        self.bg_location = os.path.join("sprites", "background.bmp")

        # Ship settings.
        self.ship_speed_multiplier = 10
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_speed_factor = 75
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 184, 20)
        self.bullets_allowed = 3

        # Alien sprites.
        self.alien_general = os.path.join("sprites", "alien_general.bmp")
        self.test = os.path.join("sprites", "test.gif")
        # self.alien_black = os.path.join("sprites", "alien_black.bmp")
        # self.alien_cyan = os.path.join("sprites", "alien_cyan.bmp")
        # self.alien_blue = os.path.join("sprites", "alien_blue.bmp")
        # self.alien_purple = os.path.join("sprites", "alien_purple.bmp")
        # self.alien_yellow = os.path.join("sprites", "alien_yellow.bmp")
        # self.alien_red = os.path.join("sprites", "alien_red.bmp")
        # self.alien_green = os.path.join("sprites", "alien_green.bmp")

        # Alien settings.
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1 right, -1 left
        self.fleet_direction = 1

import os


class Settings():
    def __init__(self):
        # Initializing game settings.
        self.screen_width = 640
        self.screen_height = 720

        # Background settings
        self.bg_color = (230, 230, 230)
        # os.path.join() for cross-platforming
        self.bg_location = os.path.join("sprites", "background.bmp")

        # Ship settings.
        self.ship_speed_multiplier = 1

        # Bullet settings.
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

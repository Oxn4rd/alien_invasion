import os


class Settings():
    def __init__(self):
        # Initializing game settings.
        self.screen_width = 480
        self.screen_height = 720

        # Background settings
        self.bg_color = (230, 230, 230)
        # os.path.join() for cross-platforming
        self.bg_location = os.path.join("sprites", "background.bmp")

        # Ship settings.
        self.ship_speed_multiplier = 10

        # Bullet settings.
        self.bullet_speed_factor = 75
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 184, 20)
        self.bullets_allowed = 3
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # Bullet class.

    def __init__(self, ai_settings, screen, ship):
        # Creating a bullet object at the ship's current position.
        super().__init__()
        self.screen = screen

        # Creating a bullet rect at (0, 0) and then setting correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Storing the bullet's postition as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

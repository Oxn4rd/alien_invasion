import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        # Initializing the ship.
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading the ship.
        self.image = pygame.transform.scale(
            pygame.image.load('./sprites/ship.bmp'), [40, 70])
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Starting each new ship at the bottom in the middle.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_multiplier
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_multiplier

    def bltime(self):
        # Drawing ship at the current location.
        self.screen.blit(self.image, self.rect)

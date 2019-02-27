import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions


# Game initialization and opening window.
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Making a ship.
    ship = Ship(ai_settings, screen)
    # Making a group to store bullets in.
    bullets = Group()
    # Making alien.
    alien = Alien(ai_settings, screen)
    # Making fleet.
    aliens = Group()

    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    # Staring main loop.
    while True:
        game_functions.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(ai_settings, screen, ship,
                                     aliens, bullets)

try:
    run_game()
except KeyboardInterrupt:
    sys.exit()

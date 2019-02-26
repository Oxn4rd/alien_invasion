import sys
import pygame

from settings import Settings
from ship import Ship
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

    # Staring main loop.
    while True:
        game_functions.check_events(ship)
        game_functions.update_screen(ai_settings, screen, ship)
        ship.update()

run_game()

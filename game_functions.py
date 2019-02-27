import sys
import pygame

from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    # Watching for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        ship.rect.centerx += 1
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        ship.rect.centerx -= 1
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_bullets(bullets):
    # Updating the position of bullets and getting rid of old bullets.
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom  <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, bullets):
    # screen.fill(ai_settings.bg_color)                              # Color
    screen.blit(pygame.image.load(ai_settings.bg_location), (0, 0))  # Image

    # Drawing bullets.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.bltime()

    # Making the most recently drawn screen visible.
    pygame.display.flip()

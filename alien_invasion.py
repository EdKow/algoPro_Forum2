import pygame #pygame installed in python 3.11.4 (to change this look at the bottom right corner)

import sys

from Settings import Settings
from ship import Ship
import game_funstions as gf
from pygame.sprite import Group

pygame.init()

FPS = 60



bg_color = (230,230,230)

def run_game():
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    
    bg_color = (230,230,230)
    ai_settings = Settings()
    
    pygame.init()
    ship = Ship(ai_settings, screen)
    bullets = Group()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            screen.fill(ai_settings.bg_color)
            ship.blitme()
            pygame.display.flip()

run_game()
        
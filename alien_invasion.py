import pygame #pygame installed in python 3.11.4 (to change this look at the bottom right corner)

import sys

from Settings import Settings
from ship import Ship
pygame.init()
screen = pygame.display.set_mode((1200,800))
FPS = 60

pygame.sprite.collide_rect(left=1, right=1)


bg_color = (230,230,230)

def run_game():
    ship = Ship(screen)

    pygame.display.set_caption("Alien Invasion")

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            screen.fill(ai_settings.bg_color)
            ship.blitme()
            pygame.display.flip()

run_game()
        
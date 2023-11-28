import pygame #pygame installed in python 3.11.4 (to change this look at the bottom right corner)

import sys
from alien import Alien
from Settings import Settings
from ship import Ship
import game_funstions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



FPS = 60

bg_color = (230,230,230)

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    play_button = Button(ai_settings, screen, "Play")
    bg_color = (230,230,230)
    
    
    
    alien = Alien(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        screen.fill(ai_settings.bg_color)

run_game()
        

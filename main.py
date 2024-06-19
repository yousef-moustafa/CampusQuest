'''
Ziad Sprint 1:
# Import necessary modules and classes
# Initialize Pygame
# Create the game settings instance
# Create the game window
# Load the game map
# Set up the game loop
    # Handle events (e.g., quit, key presses)
    # Update game logic (e.g., move player, update enemies)
    # Render the game (e.g., draw map, player, enemies)
    # Flip the display
# Quit Pygame
'''

# main.py
import os
import pygame as pg
from src.player import Player
from src.settings import Settings

pg.init()

settings = Settings()
screen = pg.display.set_mode((settings.width, settings.height))
pg.display.set_caption(settings.title)

clock = pg.time.Clock()

player = pg.sprite.GroupSingle()
player.add(Player())

# Map
from pytmx.util_pygame import load_pygame
tmx_data = load_pygame('assets/map_data/tmx/map.tmx')

# Main Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # Draw screen and add player
    screen.fill(settings.background_color)
    player.draw(screen)
    player.update()

    pg.display.flip()
    clock.tick(60)

# Quit Pygame
pg.quit()

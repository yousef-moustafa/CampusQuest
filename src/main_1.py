# main.py

import pygame as pg
from player import Player

pg.init()

screen = pg.display.set_mode((1280, 720))
pg.display.set_caption('CampusQuest')

clock = pg.time.Clock()

player = pg.sprite.GroupSingle()
player.add(Player())

# Main game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # Draw screen and add player
    screen.fill("#47b455")
    player.draw(screen)
    player.update()

    pg.display.flip()
    clock.tick(60)

# Quit Pygame
pg.quit()

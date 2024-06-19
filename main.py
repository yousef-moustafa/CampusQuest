import pygame as pg
from src.player import Player
from src.settings import Settings
from src.map_loader import MapLoader

pg.init()

settings = Settings()
screen = pg.display.set_mode((settings.width, settings.height))
pg.display.set_caption(settings.title)

clock = pg.time.Clock()

# Load the map
map_path = 'assets/map_data/tmx/map.tmx'
map_loader = MapLoader(map_path)
map_loader.load_map()
sprite_group = map_loader.get_sprite_group()

# Add player to the map
player = pg.sprite.GroupSingle()
player.add(Player())

# Main Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # Draw screen and add player
    screen.fill(settings.background_color)
    sprite_group.draw(screen)
    player.draw(screen)
    player.update()
    pg.display.flip()
    clock.tick(60)

# Quit Pygame
pg.quit()

import pygame as pg
from src.player import Player
from src.settings import Settings
from src.map_loader import MapLoader, CameraGroup, Tile

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
map_width = map_loader.get_map_width()
map_height = map_loader.get_map_height()

#Camera Group / Map
camera_group = CameraGroup(map_width, map_height, settings.width, settings.height)
for sprite in sprite_group:
    camera_group.add(sprite)

#add player to the camera group
player = Player()
camera_group.add(player)

# Main Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        #zooming with mouse
        if event.type == pg.MOUSEWHEEL:
            camera_group.zoom_scale += event.y * 0.03
            #for max zoom in/out future implementation
            #camera_group.zoom_scale = max (camera_group.min_zoom_scale, min(camera_group.zoom_scale, camera_group.max_zoom_scale))

    # check for collisions
    player.check_collisions(sprite_group)
    
    # Update player and other sprites
    player.update()
    camera_group.center_target_camera(player)

    # Draw screen with the camera view and add the player
    screen.fill(settings.background_color)
    camera_group.custom_draw(player)
    pg.display.flip()
    clock.tick(60)

# Quit Pygame
pg.quit()



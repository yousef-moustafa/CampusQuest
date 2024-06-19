import pygame as pg
from pytmx.util_pygame import load_pygame

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

class MapLoader:
    def __init__(self, map_path):
        self.map_path = map_path
        self.sprite_group = pg.sprite.Group()
    
    def load_map(self):
        tmx_data = load_pygame(self.map_path)        
        # Loop through all layers
        for layer in tmx_data.visible_layers:
            if hasattr(layer,'data'):
                for x,y,surf in layer.tiles():
                    pos = (x * 16, y * 16)
                    Tile(pos = pos, surf = surf, groups=self.sprite_group)
        for obj in tmx_data.objects:
            pos = obj.x, obj.y
            if obj.image:
                Tile(pos = pos,surf = obj.image, groups =self.sprite_group)
    
    def get_sprite_group(self):
        return self.sprite_group
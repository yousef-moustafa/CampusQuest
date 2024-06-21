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
    
    #for max map zoom out future implementation
    def get_map_width(self):
        return 88 * 16
    
    def get_map_height(self):
        return 96 * 16
    
class CameraGroup(pg.sprite.Group):
    def __init__(self, map_width, map_height, display_width, display_height):
        super().__init__()
        self.display_surface = pg.display.get_surface()

        #camera offset
        self.offset = pg.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        #zoom
        self.zoom_scale = 1
        #for max zoom in/out future implementation
        self.min_zoom_scale = 0.5
        self.max_zoom_scale = min(display_width / map_width, display_height / map_height)

        self.internal_surf_size = (2500, 2500)
        self.internal_surf = pg.Surface(self.internal_surf_size, pg.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center = (self.half_w, self.half_h))
        self.internal_surf_size_vector = pg.math.Vector2(self.internal_surf_size)
        self.internal_offset = pg.math.Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h

    def zoom_keyboard_control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_q]:
            self.zoom_scale += 0.1
        if keys[pg.K_e]:
            self.zoom_scale -= 0.1

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player):
        self.center_target_camera(player)

        #filling the internal surface
        self.internal_surf.fill('#47b455')

        self.zoom_keyboard_control()

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            self.internal_surf.blit(sprite.image, offset_pos)
        
        scaled_surf = pg.transform.scale(self.internal_surf, self.internal_surf_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center = (self.half_w, self.half_h))
        self.display_surface.blit(scaled_surf, scaled_rect)



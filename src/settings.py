class Settings:
    
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.title = 'Campus Quest'
        self.background_color = '#47b455'
        self.player_speed = 7    
        
    # ability to adjust default settings
    def set_screen_resolution(self, width, height):
        if width > 0 and height > 0:
            self.screen_width = width
            self.screen_height = height

    def set_background_color(self, color):
        self.background_color = color
        
    def set_grid_size(self, size):
        if size > 0: self.grid_size = size

    def set_player_speed(self, speed):
        if speed > 0: self.player_speed = speed
        
    
    def reset(self):
        self.width = 1280
        self.height = 720
        self.title = 'Campus Quest'
        self.background_color = (0, 0, 0)
        self.grid_size = 20
        self.player_speed = 10

        
        
        
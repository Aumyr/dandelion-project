import pygame, os

class Button():
    def __init__(self, button_text = "Sample text!", font_path = os.path.join("..", "ASSETS", "FONTS", "Anonymous.ttf"), font_size = 20):
        self.button_text = button_text
        self.font_path = font_path
        self.font_size = font_size

        #self.button_text = pygame.font.Font(self.font_path, self.font_size)

    def set_button_text(self, button_text):
        self.button_text = button_text

    def set_button_font(self, font_path):
        self.font_path = font_path

    def set_button_font_size(self, font_size):
        self.font_size = font_size

    def get_button_font(self):
        #return pygame.font.Font(self.font_path, self.font_size)
        return pygame.font.SysFont('Arial',self.font_size)
        
    def get_button(self):  
        return self.get_button_font().render(self.button_text, 1, (255,255,0))

    @DeprecationWarning
    def transform(self):
        self.button_text = pygame.font.Font(self.font_path, self.font_size)

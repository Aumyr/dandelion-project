import pygame

class Image():
    def __init__(self, path = "../ASSETS/IMAGES/NOIMAGE.png"):    
        self.image = pygame.image.load(path)

    def get_image_size(self):
        return self.image.get_rect().size

    def get_width(self):
        return self.image.get_rect().size[0]

    def get_height(self):
        return self.image.get_rect().size[1]

    def set_image_size(self, width, height):
        self.set_height(height)
        self.set_width(width)

    def set_height(self, height):
        self.image = pygame.transform.scale(self.image, (self.get_width(), height))
        self.width, self.height = self.image.get_rect().size

    def set_width(self, width):
        self.image = pygame.transform.scale(self.image, (width, self.get_height()))
        self.width, self.height = self.image.get_rect().size

    def get_image(self):
        return self.image
    

import pygame
from image import Image
from button import Button

default_width = 2560
default_height = 1600

pygame.init()
display = pygame.display.set_mode((default_width, default_height), pygame.RESIZABLE)
width, height = pygame.display.get_surface().get_size()

pygame.display.set_caption("Dandelion Crusade")
clock = pygame.time.Clock()

intro_song = pygame.mixer.Sound("../ASSETS/AUDIO/INTRO.WAV")
intro_background = pygame.image.load("../ASSETS/IMAGES/START_SCREEN.GIF")
game_title = pygame.image.load("../ASSETS/IMAGES/TITLE.png")

intro_song.play()

testeo = Image("../ASSETS/IMAGES/TITLE.png")
testeo.set_image_size(2000,200)

boton_de_prueba = Button("What if you eat me toa la alcaparra")

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #intro_song.fadeout(2000)
            crashed = True
        print(event)
    pygame.display.flip()
    
    intro_background = pygame.transform.scale(intro_background, (width, height))
    display.blit(intro_background,(0,0))
    display.blit(testeo.get_image(),(230,90))
    display.blit(boton_de_prueba.get_button(),(500,500))

    clock.tick(60)
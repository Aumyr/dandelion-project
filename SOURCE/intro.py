import pygame

default_width = 800
default_height = 600

pygame.init()

display = pygame.display.set_mode((default_width, default_height), pygame.RESIZABLE)

width, height = pygame.display.get_surface().get_size()

pygame.display.set_caption("TEST")
clock = pygame.time.Clock()

intro_song = pygame.mixer.Sound("../ASSETS/AUDIO/INTRO.WAV")
intro_background = pygame.image.load("../ASSETS/IMAGES/START_SCREEN.GIF")

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro_song.fadeout(2000)
            crashed = True
        print(event)
    pygame.display.flip()
    intro_song.play()
    intro_background = pygame.transform.scale(intro_background, (width, height))
    w, h = pygame.display.get_surface().get_size()
    display.blit(intro_background,(0,0))
    clock.tick(600)

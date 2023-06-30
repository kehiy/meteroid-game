import pygame

pygame.init()

#  window size:
display_width = 800
display_height = 600

# images: 
bg = pygame.image.load('./public/bg.png')
space_craft = pygame.image.load('./public/space_craft.png')
meteor_obj = pygame.image.load('./public/meteor.png')
icon = pygame.image.load('./public/icon1.png')

# sounds:
pygame.mixer.music.load("./public/world-m.ogg")
crash_sound = pygame.mixer.Sound("./public/lose-m.wav")

# display:
display = pygame.display.set_mode((display_width, display_height))

# other:
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

craft_width = 48

clock = pygame.time.Clock()

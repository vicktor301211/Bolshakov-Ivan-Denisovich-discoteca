import random

from pygame.draw import circle

from all_colors import *
import pygame
pygame.init()

#pygame.mixer.init()
#pygame.mixer.music.load('music.mp3')
#pygame.mixer.music.play(-1)

size = (1280, 740)
pygame.display.set_caption('Домашняя дискотека')
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen.fill((255, 255, 255))
BACKGROUND = (255, 255, 255)
x = 0
y = 0
color = COLORS
timer = 0
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    color_index = random.randint(0, 7)
    if color_index == 7:
        BACKGROUND = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    else:
        BACKGROUND = COLORS[color_index]

    for i in range(10):
        x = random.randint(0, 1280)
        y = random.randint(0, 740)
        radius = random.randint(10, 100)
        color = COLORS
        pygame.draw.circle(screen, random.choice(color), (x, y), radius)

    screen.fill(BACKGROUND)
    pygame.display.flip()
    pygame.time.delay(random.randint(200, 800))


pygame.quit()
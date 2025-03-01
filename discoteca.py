import pygame
import random
from all_colors import *
pygame.init()

#pygame.mixer.init()
#pygame.mixer.music.load('music.mp3')
#pygame.mixer.music.play(-1)

size = (0, 0)
pygame.display.set_caption('Домашняя дискотека')
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
BACKGROUND = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0)]
running = True
timer = 0
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
        x = random.randint(0, 0)
        y = random.randint(0, 0)
        radius = random.randint(10, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.circle(screen, color, (x, y), radius)

    screen.fill(BACKGROUND)
    pygame.display.flip()
    pygame.time.delay(random.randint(200, 800))

pygame.quit()
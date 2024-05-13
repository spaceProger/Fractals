import pygame
import numpy as np


fps = 60

max_iteration = 50

k = .003
kd = 10

size = (1920, 1080) 
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

def pixel(pos: tuple[int], k_c:float):
    color = np.array([255, 255, 255]) * k_c
    pygame.draw.circle(screen, color, pos, radius=1)

def fractal():
    for x in range(size[0] + 1):
        for y in range(size[1] + 1):
            kx = (x - size[0] / 2 - 200) * k
            ky = (y - size[1] / 2) * k
            c = kx + ky * 1j
            z = 0
            for iteration in range(max_iteration):
                z = z ** 2 + c
                if abs(z) > 4:
                    k_c = iteration / max_iteration
                    pixel((x, y), k_c)
                    break
        pygame.display.update()

change = True

while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                k /= kd
            elif event.button == 5:
                k *= kd
            change = True
    
    if change:
        screen.fill((0, 0, 0))
        fractal()
        change = False


import pygame

screen = pygame.display.set_mode((1000, 800))

def fade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((255, 255, 255))
    for a in range(0, 200):
        fade.set_alpha(a)
        redrawWindow()
        print(a)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

def redrawWindow():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (200, 300, 200, 200), 0)
    pygame.draw.rect(screen, (0, 255, 0), (500, 500, 100, 200), 0)

run = True

while run:
    redrawWindow()
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            fade(500, 800)


        pygame.display.update()


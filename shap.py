import pygame
import random

from pygame.draw import rect

pygame.init()

screen_width = 900
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("1010 게임 도형 그려보기")


shap = (
    ((0, 0, 1),     
    (0, 0, 1), 
    (1, 1, 1)),
    ((0, 0, 0),
     (0, 1, 0),
     (0, 1, 0)),
     ((0, 0, 0),
     (0, 0, 0),
     (1, 1, 1)),
    ((1, 1, 1),     
    (1, 1, 1), 
    (1, 1, 1)),
     ((1, 1, 1),
     (0, 0, 1),
     (0, 0, 1)),
    ((0, 0, 0),
     (1, 0, 0),
     (1, 1, 1)),
    ((0, 1, 0),
     (0, 1, 0),
     (0, 1, 0)),
    ((1, 0, 0),
     (1, 0, 0),
     (1, 1, 1)),
)

shap_size = 45
shap_len = 3

random_block = []

running = True

for i in range(3):
    random_block.append(random.randrange(0, 8))

print(random_block)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for idx, val in enumerate(tuple(random_block)):
        for y in range(shap_len):
            for x in range(shap_len):
                if shap[val][y][x] == 0:
                    continue
                pygame.draw.rect(screen, (255, 255, 255), (
                        shap_size*x + (idx*shap_size*3.5), shap_size*y, shap_size, shap_size
                ), 1)

    
    pygame.display.update()

pygame.quit()

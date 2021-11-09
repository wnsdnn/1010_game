# import math

# FILED_PIECE_SIZE = 35

# def cordinates(num):
#     n =  num % FILED_PIECE_SIZE
#     result = num / FILED_PIECE_SIZE
#     if n > FILED_PIECE_SIZE / 2:
#         return math.ceil(result)
#     else:
#         return math.floor(result)

# aa = 236
# print(cordinates(aa), aa / 35)



# option = []

# op = True
# for i in range(3):
#     option.append(op)

# print(option)


# import json

# with open("C:/Users/User/Desktop/1010_game/js/record.json") as json_file:
#     json_data = json.load(json_file)

#     score_obj = json_data["score_object"]["score"]
#     print(score_obj)







import asyncio
import pygame
import time


# async def factorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         print(f"Task {name}: Compute factorial({number}), currently i={i}...")
#         await asyncio.sleep(1)
#         f *= i
#     print(f"Task {name}: factorial({number}) = {f}")
#     return f

# async def main():
#     # Schedule three calls *concurrently*:
#     L = await asyncio.gather(
#         factorial("A", 2),
#         factorial("B", 3),
#         factorial("C", 4),
#     )
#     print(L)

# asyncio.run(main())

screen_width = 600
screen_height = 790
screen = pygame.display.set_mode((screen_width, screen_height))

array = (
    (10, 10, 50, 50),
    (100, 10, 50, 50),
    (200, 10, 50, 50),
    (10, 100, 50, 50),
    (10, 200, 50, 50)
)

async def fade(data):
    fade = pygame.Surface((data[2], data[3]))
    fade.fill((0, 0, 0))
    await asyncio.sleep(1)
    for a in range(0, 200):
        fade.set_alpha(a)
        screen.blit(fade, (data[0], data[1]))
        pygame.display.update()

async def aa():
     await asyncio.gather(
        fade(array[0]),
        fade(array[1]),
        fade(array[2]),
        fade(array[3]),
        fade(array[4]),
    )


def draw():
    for data in array:
        pygame.draw.rect(screen, (0, 255, 0), (data[0], data[1], data[2], data[3]), 0)




run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        asyncio.run(aa())
        # for data in array:
        #     asyncio.run(fade(data[0], data[1], data[2], data[3]))

    screen.fill((255, 255, 255))
    draw()
    

    pygame.display.update()

pygame.quit()




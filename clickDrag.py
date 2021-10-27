import pygame

from pygame.constants import BUTTON_LEFT

class Key(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, id):
        super(Key, self).__init__()
        self.image = pygame.image.load("C:\\Users\\User\\Desktop\\1010_game\\button.png").convert()
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.id = id
        self.linkReady = False
        self.links = []


pygame.init()

size = (700, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("This is a new window")

done = False

clock = pygame.time.Clock()

key_list = pygame.sprite.Group()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            if event.button == 3:
                key_list.add(Key(x, y, len(key_list)+1))
                # event.button == ?
                # 1: left click
                # 2: middle click
                # 3: right click
                # 4: scroll up
                # 5: scroll down
            elif event.button == 1:
                for key in key_list:
                    if key.rect.collidepoint(pos):
                        key.clicked = True
            elif event.button == 2:
                for key in key_list:
                    if key.rect.collidepoint(pos):
                        key.linkReady = True
                        count = 0
                        links = []
                        for key in key_list:
                            if key.linkReady == True:
                                count += 1
                                links.append(key.id)
                        if count == 2:
                            for key in key_list:
                                if key.linkReady == True:
                                    key.linkReady = False
                                    count += 1
                                    key.links += links
        
        if event.type == pygame.MOUSEBUTTONUP:
            for key in key_list:
                key.clicked = False
            drag_id = 0
    
    for key in key_list:
        if key.clicked == True:
            pos = pygame.mouse.get_pos()
            key.rect.x = pos[0] - (key.rect.width/2)
            key.rect.y = pos[1] - (key.rect.height/2)
    
    screen.fill((0, 0, 0))

    key_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()


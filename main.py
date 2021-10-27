from os import O_NDELAY
import pygame
import random

pygame.init()

# 전역 변수들
screen_width = 550
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

# xx = 0
# yy = 0
# start_x = 0
# start_y = 0
# md = False

game_font = pygame.font.Font(None, 40)

pygame.display.set_caption("1010 game")

clock = pygame.time.Clock()


running = True
FILED = []
FILED_WIDTH = 8
FILED_HEIGHT = 8
FILED_COLOR = (0, 0, 0)
FILED_PIECE_SIZE = 45
FILED_X_POS = (screen_width / 2) - (FILED_PIECE_SIZE * FILED_WIDTH) / 2
FILED_Y_POS = FILED_PIECE_SIZE * 2
score = 0
score_str = "Score: %s" % (score)


# class Block():
#     def __init__(self, num, xpos, ypos, id):
#         self.id = id
#         self.image = pygame.image.load("C:\\Users\\User\\Desktop\\1010_game\\image\\block%s.png" % (num+1))
#         self.clicked = False
#         self.xpos = xpos
#         self.ypos = ypos
#         self.rect = self.image.get_rect()

blocks = (
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

shape_width = 3
shape_height = 3
random_block = []


# 게임판 정보를 FILED라는 리스트 안에 집어넣기
def set_filed():
    for i in range(FILED_HEIGHT):
        FILED.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# 게임판을 그리는 함수
def draw_filed():
    for y in range(FILED_HEIGHT):
        for x in range(FILED_WIDTH):
            val = FILED[y][x]
            line_width = 1
            
            # 해당 값이 0이 아니라면 검은색으로 색칠
            if val != 0:
                line_width = 0

            pygame.draw.rect(screen, (0, 0, 0),
            (
                FILED_X_POS + x*FILED_PIECE_SIZE,
                FILED_Y_POS + y*FILED_PIECE_SIZE,
                FILED_PIECE_SIZE,
                FILED_PIECE_SIZE
            )
            , line_width)

# 게임에 사용할 도형 3개 배열에 넣는 함수
def set_block():
    for i in range(3):
        random_block.append(random.randrange(0, 8))


# 처음 세팅할 도형을 그려주는 함수
def draw_block():
    block_height = screen_height - 190
    for idx, val in enumerate(tuple(random_block)):
        for y in range(shape_height):
            for x in range(shape_width):
                if blocks[val][y][x] == 0:
                    continue
                pygame.draw.rect(screen, (0, 0, 0), (
                        FILED_PIECE_SIZE*x + (idx*FILED_PIECE_SIZE*3.7) + 50
                        , FILED_PIECE_SIZE*y + block_height, FILED_PIECE_SIZE, FILED_PIECE_SIZE
                ), 1)


# 게임 실행
set_filed()

print(random_block)
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # 배경색 칠하기
    screen.fill((225, 255, 255))

    

    # 마우스 이벤트
    # if event.type == pygame.MOUSEBUTTONDOWN:
    #     if rect_box.collidepoint(event.pos):
    #         start_x = pygame.mouse.get_pos()[0]
    #         start_y = pygame.mouse.get_pos()[1]
    #         md = True

    # if md and event.type ==  pygame.MOUSEMOTION:
    #     xx = pygame.mouse.get_pos()[0] - start_x
    #     yy = pygame.mouse.get_pos()[1] - start_y

    # if event.type == pygame.MOUSEBUTTONUP:
    #     md = False
    #     xx = 0
    #     yy = 0
    #     start_x = 0
    #     start_y = 0

    
    # 현재 점수 나타내기
    total_score = game_font.render(score_str, True, (0, 0, 0))
    screen.blit(total_score, (FILED_PIECE_SIZE/2, FILED_PIECE_SIZE/2))

    # 게임판 그리는 함수
    if len(random_block) <= 0:
        set_block()

    draw_filed()
    draw_block()
    
    pygame.display.update()

    
pygame.quit()
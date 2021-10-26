import pygame
from pygame.draw import rect

pygame.init()

# 전역 변수들
screen_width = 550
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))


xx = 0
yy = 0
f_xx = 0
f_yy = 0
l_xx = 0
l_yy = 0
md = False

game_font = pygame.font.Font(None, 40)

pygame.display.set_caption("1010 game")

clock = pygame.time.Clock()


running = True
FILED = []
FILED_WIDTH = 8
FILED_HEIGHT = 8
FILED_PIECE_SIZE = 45
FILED_X_POS = (screen_width / 2) - (FILED_PIECE_SIZE * FILED_WIDTH) / 2
FILED_Y_POS = FILED_PIECE_SIZE * 2
score = 0
score_str = "Score: %s" % (score)



# rects = [
#     {
#         "x_pos": 75,
#         "y_pos": 10,
#         "width": 50,
#         "height": 20
#     },
#     {
#         "x_pos": 75,
#         "y_pos": 100,
#         "width": 50,
#         "height": 20
#     }
# ]

# 게임판 정보를 FILED라는 리스트 안에 집어넣기
def set_filed():
    for i in range(FILED_HEIGHT):
        FILED.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# 게임판을 그리는 함수
def draw_filed():
    for y in range(FILED_HEIGHT):
        for x in range(FILED_WIDTH):
            val = FILED[y][x]
            color = (40, 40, 40)
            pygame.draw.rect(screen, color,
            (
                FILED_X_POS + x*FILED_PIECE_SIZE,
                FILED_Y_POS + y*FILED_PIECE_SIZE,
                FILED_PIECE_SIZE,
                FILED_PIECE_SIZE
            )
            , 1)


# 게임 실행
set_filed()
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # if 
            print("MouseDown")
            # print(pygame.mouse.get_pos())
            f_xx = pygame.mouse.get_pos()[0]
            f_yy = pygame.mouse.get_pos()[1]
            md = True
            # pass
        if md and event.type ==  pygame.MOUSEMOTION:
            xx = pygame.mouse.get_pos()[0] - f_xx
            yy = pygame.mouse.get_pos()[1] - f_yy
            # print(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            md = False
            xx = 0
            yy = 0
            f_xx = 0
            f_yy = 0


    rect_box_width = 480
    rect_box_height = 150
    rect_box_x_pos = (screen_width / 2) - (rect_box_width / 2)
    rect_box_y_pos = screen_height - rect_box_height - 50

    screen.fill((225, 255, 255))
    # for rect_idx, rect_val in enumerate(rects):


    pygame.draw.rect(screen, (0, 0, 0, 0), (rect_box_x_pos + xx, rect_box_y_pos + yy, rect_box_width, rect_box_height), 1)

    total_score = game_font.render(score_str, True, (0, 0, 0))
    screen.blit(total_score, (FILED_PIECE_SIZE/2, FILED_PIECE_SIZE/2))

    
    draw_filed()
    
    pygame.display.update()
  
        
pygame.quit()
import pygame
import random
import math

pygame.init()

# 전역 변수들
screen_width = 550
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))


game_font = pygame.font.Font(None, 40)

pygame.display.set_caption("1010 game")

clock = pygame.time.Clock()

# 게임이 실행중인지를 판별하는 변수
running = True

# 게임판 관련 변수들
FILED = []  # 게임판
FILED_WIDTH = 8  # 게임판의 넓이
FILED_HEIGHT = 8  # 게임판의 높이
FILED_COLOR = (0, 0, 0)  # 게임판의 색깔
FILED_PIECE_SIZE = 45  # 게임판에 들어가는 사각형의 크기

# x, y 좌표
FILED_X_POS = (screen_width / 2) - (FILED_PIECE_SIZE * FILED_WIDTH) / 2
FILED_Y_POS = FILED_PIECE_SIZE * 2
# 도형들의 y좌표
block_y_pos = screen_height - 190
# 점수
score = 0
score_str = "Score: %s" % (score)

# 도형의 기본 크기 3*3
block_width = 3
block_height = 3

# 도형의 모양(번호)?이 랜덤으로 들어갈 리스트
random_block = []

# 도형이 들어갈 리스트
block_list = []

# 마우스를 클릭한 좌표
start_to_x = 0
start_to_y = 0

# 현재 마우스의 좌표
mouse_to_x = 0
mouse_to_y = 0

# 마우스 다운 되었있는지를 판별하는 함수
md = False

# 도형들의 인덱스 번호와 모양 정보가 있는 변수들
block_id = 100
block_num = 100

# 클릭한 도형의 사각형 인덱스 값
click_block_list = 0

# 도형들의 모양들
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

# 도형들 만드는 클래스
class Block():
    def __init__(self, xpos, ypos, id, num, list):
        self.rect = 0
        self.id = id
        self.xpos = xpos
        self.ypos = ypos
        self.num = num
        self.list = (list)

    def get_rect(self, rect):
        self.rect = rect

    def draw_block(self, mouse_xpos, mouse_ypos, id):
        xpos = 0
        ypos = 0
        if self.id == id:
            xpos = mouse_xpos
            ypos = mouse_ypos
        block = pygame.draw.rect(screen, (0, 0, 0), (self.xpos + xpos, self.ypos + ypos, FILED_PIECE_SIZE, FILED_PIECE_SIZE))
        return block


# 게임판 정보를 FILED라는 리스트 안에 집어넣기
def set_filed():
    for i in range(FILED_HEIGHT):
        FILED.append([0, 0, 0, 0, 0, 0, 0, 0])

# 게임판을 그리는 함수
def draw_filed():
    for y in range(FILED_HEIGHT):
        for x in range(FILED_WIDTH):
            val = FILED[y][x]
            line_width = 1
            
            # 해당 값이 0이 아니라면 검은색으로 색칠
            if val != 0:
                line_width = 0

            pygame.draw.rect(screen, (0, 0, 0), (
                FILED_X_POS + y*FILED_PIECE_SIZE,
                FILED_Y_POS + x*FILED_PIECE_SIZE,
                FILED_PIECE_SIZE,
                FILED_PIECE_SIZE ), line_width)

# 게임에 사용할 도형 3개 배열에 넣는 함수
def set_block():
    for i in range(3):
        random_block.append(random.randrange(0, 8))


# 도형을 그려 넣는 함수
def draw_block():
    for idx, val in enumerate(tuple(random_block)):
        for y in range(block_height):
            for x in range(block_width):
                if blocks[val][y][x] == 0:
                    continue
                block = Block(FILED_PIECE_SIZE*x + (idx*FILED_PIECE_SIZE*3.7) + 50, FILED_PIECE_SIZE*y + block_y_pos, idx, val, (x, y))
                block_rect = block.draw_block(mouse_to_x, mouse_to_y, block_id)
                block.get_rect(block_rect)
                block_list.append(block)


def cordinates(num):
    result = num / FILED_PIECE_SIZE
    return math.floor(result)


def line_delete():
    # for y in range(FILED_HEIGHT):
    #     yy = 0
    #     for x in range(FILED_WIDTH):
    #         if FILED[y][x] == 1:
    #             yy += 1
    #     if yy >= FILED_HEIGHT:
    #         FILED[y] = [0, 0, 0, 0, 0, 0, 0, 0]
    for y in range(FILED_HEIGHT):
        xx = 0
        for x in range(FILED_WIDTH):
            if FILED[x][y] == 1:
                xx += 1
            if xx >= FILED_WIDTH:
                FILED[x][y] == 0


# 게임 실행
set_filed()

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 마우스 이벤트
    if event.type == pygame.MOUSEBUTTONDOWN:
        md = True
        start_to_x = pygame.mouse.get_pos()[0]
        start_to_y = pygame.mouse.get_pos()[1]

        for block in block_list:
            if block.rect.collidepoint(event.pos):
                # print(block.list)
                click_block_list = block.list
                block_id = block.id
                block_num = block.num

        # for block in blocks[block_num]:
        #     print(block)
        

    if md and event.type == pygame.MOUSEMOTION:
        mouse_to_x = pygame.mouse.get_pos()[0] - start_to_x
        mouse_to_y = pygame.mouse.get_pos()[1] - start_to_y


    if md and event.type == pygame.MOUSEBUTTONUP:
        # 게임판 기준으로 현재 마우스의 위치
        block_x = cordinates(pygame.mouse.get_pos()[0] - FILED_X_POS)
        block_y = cordinates(pygame.mouse.get_pos()[1] - FILED_Y_POS)


        if click_block_list != 0 and block_x <= 7 and block_y <= 7 and block_x >= 0 and block_y >= 0:
            # 게임판에 그릴 도형의 0, 0 시작 위치
            start_x = block_x - click_block_list[0]
            start_y = block_y - click_block_list[1]
            for y in range(block_height):
                for x in range(block_width):
                    block_con = blocks[block_num][y][x]
                    if block_con == 0:
                        continue
                    FILED[start_x + x][start_y + y] = 1
            del random_block[block_id]

        # 값 초기화
        md = False
        start_to_x = 0
        start_to_y = 0
        mouse_to_x = 0
        mouse_to_y = 0
        block_id = 100
        block_num = 100
        click_block = 0
    
    # 배경색 칠하기
    screen.fill((225, 255, 255))

    

    # 도형 3개를 다 쓰면 다시 도형 만드는 함수
    if len(random_block) <= 0:  
        set_block()

    # 게임판이랑 도형 그리기
    draw_filed()
    draw_block()
    line_delete()

    # 현재 점수 나타내기
    total_score = game_font.render(score_str, True, (0, 0, 0))
    screen.blit(total_score, (FILED_PIECE_SIZE/2, FILED_PIECE_SIZE/2))
    

    # running = False
    pygame.display.update()

    
pygame.quit()
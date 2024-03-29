# python 3.7.2
# pip install pygame
import pygame
import json
import random
import math

from pygame.rect import Rect

pygame.init()

# 전역 변수들
best_score = 0

with open("C:/Users/User/Desktop/1010_game/js/record.json") as json_file:
    json_data = json.load(json_file)
    score_obj = json_data["score"]

    for score in score_obj:
        if best_score <= score:
            best_score = score

level = 1
level_up = 0

popup_on = False

screen_width = 600
screen_height = 790
screen = pygame.display.set_mode((screen_width, screen_height)) 
screen_rect = screen.get_rect()

game_score_font = pygame.font.Font(None, 40)
game_over_font = pygame.font.Font(None, 80)
best_score_font = pygame.font.Font(None, 27)
level_font = pygame.font.Font(None, 32)

pygame.display.set_caption("1010 game")

clock = pygame.time.Clock()

logo = pygame.image.load("C:/Users/User/Desktop/1010_game/image/logo.png")
logo_width = 180
logo_height = 53
logo_xpos = (screen_width / 2) - (logo_width / 2)
logo_ypos = 20


# 게임이 실행중인지를 판별하는 변수
running = True

count = 0
# 게임판 관련 변수들
FILED = []  # 게임판
FILED_WIDTH = 10  # 게임판의 넓이
FILED_HEIGHT = 10  # 게임판의 높이
FILED_COLOR = (0, 0, 0)  # 게임판의 색깔
FILED_PIECE_SIZE = 45  # 게임판에 들어가는 사각형의 크기

# x, y 좌표
FILED_X_POS = (screen_width / 2) - (FILED_PIECE_SIZE * FILED_WIDTH) / 2
FILED_Y_POS = FILED_PIECE_SIZE * 2.3
# 도형들의 y좌표
block_y_pos = FILED_PIECE_SIZE*FILED_HEIGHT + FILED_Y_POS
# 점수
score = 0

# 도형의 기본 크기 3*3
block_width = 4
block_height = 4
block_len = 3

# 도형의 모양(번호)?이 랜덤으로 들어갈 리스트
random_block = []

# 도형들이 들어갈 리스트
block_list = []
borad_list = []

# 마우스를 클릭한 좌표
start_to_x = 0
start_to_y = 0

# 현재 마우스의 좌표
mouse_to_x = 0
mouse_to_y = 0
block_cor = 0

# 마우스 다운 되었있는지를 판별하는 함수
md = False
mu = False

# 도형들의 인덱스 번호와 모양 정보가 있는 변수들
block_id = 100
block_num = 100
block_color = 100

# 클릭한 도형의 사각형 인덱스 값
click_block_list = 0

game_result = "Game Over"

# 색깔
COLOR = (
    (255, 0, 0),        # RED
    (117, 255, 0),      # YELLOW GREEN
    (255, 168, 0),      # ORANGE
    (0, 0, 255),        # BLUE
    (0, 128, 0),        # GREEN
    (102, 0, 153),      # PURUL
    (255, 52, 123),    # PINK
)

GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 도형들의 모양들
blocks = (
    # 0번째는 아무것도 없음(도형을 사용해도 안 밀리도록 도형 사용시 0번째 지정)
    ((0, 0, 0, 0),     
     (0, 0, 0, 0),    # 0
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 7, 7, 0),
     (0, 0, 0, 0),    # 7
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 3, 3, 0),
     (0, 3, 0, 0),    # 10
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 4, 4, 0),
     (0, 0, 4, 0),    # 11
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 2, 2, 0),
     (0, 2, 2, 0),    # 16
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 6, 0, 0),
     (6, 6, 6, 0),    # 13
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((1, 1, 1, 0),
     (0, 0, 0, 0),    # 21
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 2, 0, 0),
     (0, 2, 0, 0),    # 22
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 0, 3, 0),
     (0, 3, 3, 0),    # 23
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
)

level2 = (
    ((2, 2, 2, 2),
     (0, 0, 0, 0),    # 2
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 6, 0, 0),
     (0, 6, 0, 0),    # 6
     (0, 6, 0, 0),    
     (0, 6, 0, 0)),
    ((0, 1, 0, 0),
     (0, 0, 0, 0),    # 8
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((3, 3, 3, 0),
     (0, 0, 3, 0),    # 21
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
)
level3 = (
    ((0, 7, 0, 0),
     (0, 7, 0, 0),    # 14
     (7, 7, 0, 0),
     (0, 0, 0, 0)), 
    ((0, 1, 0, 0),
     (0, 1, 0, 0),    # 15
     (0, 1, 1, 0),    
     (0, 0, 0, 0)),
    ((0, 3, 3, 0),
     (0, 0, 3, 0),    # 17
     (0, 0, 3, 0),    
     (0, 0, 0, 0)),
    ((0, 4, 4, 0),
     (0, 4, 0, 0),    # 18
     (0, 4, 0, 0),    
     (0, 0, 0, 0)),
)
level4 = (
    ((0, 0, 1, 0),     
     (0, 0, 1, 0),    # 1
     (1, 1, 1, 0),
     (0, 0, 0, 0)),
    ((4, 4, 4, 0),
     (0, 0, 4, 0),    # 4
     (0, 0, 4, 0),    
     (0, 0, 0, 0)),
    ((5, 0, 0, 0),   
     (5, 0, 0, 0),    # 5
     (5, 5, 5, 0),
     (0, 0, 0, 0)), 
    ((3, 3, 3, 0),    
     (3, 3, 3, 0),    # 3
     (3, 3, 3, 0),    
     (0, 0, 0, 0)),
)
level5 = (
    ((0, 2, 0, 0),
     (2, 2, 2, 0),    # 9
     (0, 2, 0, 0),    
     (0, 0, 0, 0)),
    ((5, 5, 5, 0),
     (0, 5, 0, 0),    # 12
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 0, 5, 0),
     (0, 5, 5, 0),    # 19
     (0, 0, 5, 0),    
     (0, 0, 0, 0)),
    ((0, 6, 0, 0),
     (0, 6, 6, 0),    # 20
     (0, 6, 0, 0),    
     (0, 0, 0, 0)),
)

# 도형들 만드는 클래스
class Borad():
    def __init__(self, xpos, ypos, line):
        self.rect = 0
        self.xpos = xpos
        self.ypos = ypos
        self.line = line

    def get_rect(self, rect):
        self.rect = rect

    def draw_borad(self, color):
        block = pygame.draw.rect(screen, color, (self.xpos, self.ypos, FILED_PIECE_SIZE, FILED_PIECE_SIZE), self.line)
        return block

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

    def draw_block(self, mouse_xpos, mouse_ypos, id, color, line):
        xpos = 0
        ypos = 0
        if self.id == id:
            xpos = mouse_xpos
            ypos = mouse_ypos
        block = pygame.draw.rect(screen, color, (self.xpos + xpos, self.ypos + ypos, FILED_PIECE_SIZE, FILED_PIECE_SIZE), line)
        return block


# 게임판 정보를 FILED라는 리스트 안에 집어넣기
def set_filed():
    for i in range(FILED_HEIGHT):
        FILED2 = []
        for j in range(FILED_WIDTH):
            FILED2.append(0)
        FILED.append(FILED2)  

# 게임판을 그리는 함수
def draw_filed():
    for y in range(FILED_HEIGHT):
        for x in range(FILED_WIDTH):
            val = FILED[y][x]
            block_color = BLACK
            line_width = 1
            
            # 해당 값이 0이 아니라면 색칠
            if val != 0:
                line_width = 0
                block_color = COLOR[val - 1]
            borad = Borad(FILED_X_POS + y*FILED_PIECE_SIZE, FILED_Y_POS + x*FILED_PIECE_SIZE, line_width)
            borad_rect = borad.draw_borad(block_color)
            borad.get_rect(borad_rect)
            borad_list.append(borad)

def draw_filed2():
    for y in range(FILED_HEIGHT):
        for x in range(FILED_WIDTH):
            val = FILED[y][x]
            block_color = BLACK
            line_width = 1
            
            # 해당 값이 0이 아니라면 색칠
            borad = Borad(FILED_X_POS + y*FILED_PIECE_SIZE, FILED_Y_POS + x*FILED_PIECE_SIZE, line_width)
            borad_rect = borad.draw_borad(block_color)
            borad.get_rect(borad_rect)
            borad_list.append(borad)
            

# 게임에 사용할 도형 3개 배열에 넣는 함수
def set_block():
    for i in range(block_len):
        random_block.append(random.randrange(1, len(blocks)))


# 도형을 그려 넣는 함수
def draw_block():
    for idx, val in enumerate(tuple(random_block)):
        for y in range(block_height):
            for x in range(block_width):
                if blocks[val][y][x] == 0:
                    continue
                else:
                    block_color = blocks[val][y][x]
                block_size, arr = size(blocks, val)
                block_y_len = block_size[3] - block_size[2] + 1

                block = Block(
                    FILED_PIECE_SIZE*x + idx*(FILED_PIECE_SIZE*4) + idx*15 + 25, 
                    FILED_PIECE_SIZE*y + block_y_pos + ((FILED_PIECE_SIZE*(4 - block_y_len)) / 2 + 30),
                    idx, val, (x, y))
                color = COLOR[block_color - 1]
                block_rect = block.draw_block(mouse_to_x, mouse_to_y, block_id, color, 0)
                block.get_rect(block_rect)
                block_list.append(block)

def draw_block2():
    for idx, val in enumerate(tuple(random_block)):
        for y in range(block_height):
            for x in range(block_width):
                if blocks[val][y][x] == 0:
                    continue
                block_size, arr = size(blocks, val)
                block_y_len = block_size[3] - block_size[2] + 1

                block = Block(
                    FILED_PIECE_SIZE*x + idx*(FILED_PIECE_SIZE*4) + idx*15 + 25, 
                    FILED_PIECE_SIZE*y + block_y_pos + ((FILED_PIECE_SIZE*(4 - block_y_len)) /2 + 30), 
                    idx, val, (x, y))
                block_rect = block.draw_block(mouse_to_x, mouse_to_y, block_id, (0, 0, 0), 1)
                block.get_rect(block_rect)


def cordinates(num1, num2):
    rest_cor =[(num1 - block_cor[0]) % FILED_PIECE_SIZE, (num2 - block_cor[1]) % FILED_PIECE_SIZE]
    share = ((num1 - block_cor[0]) / FILED_PIECE_SIZE, (num2 - block_cor[1]) / FILED_PIECE_SIZE)
    result = []
    for idx, val in enumerate(rest_cor):
        if rest_cor[idx] >= FILED_PIECE_SIZE / 2:
            result.append(math.ceil(share[idx]))
        else:
            result.append(math.floor(share[idx]))

    return result

def size(blocks, num):
    block_result = []
    for y in range(len(blocks[num])):
        for x in range(len(blocks[num][y])):
            if blocks[num][y][x] != 0:
                block_result.append((x, y))
    min_x, min_y = block_width - 1, block_width - 1
    max_x, max_y = 0, 0
    for i in block_result:
        if min_x > i[0]:
            min_x = i[0]
        if max_x < i[0]:
            max_x = i[0]
        if min_y > i[1]:
            min_y = i[1]
        if max_y < i[1]:
            max_y = i[1]
    result = ((min_x, max_x, min_y, max_y), block_result)
    return result


def gameover():
    option = []
    for idx, random_num in enumerate(random_block):
        if random_num == 0:
            continue
        block_size, arr = size(blocks, random_num)
        block_y_len = block_size[3] - block_size[2] + 1
        block_x_len = block_size[1] - block_size[0] + 1
        
        overlap = False
        # 게임판 10*10 총 100개의 게임판에서 가로 세로 도형의 크기를 빼고 연산
        for filed_y in range(FILED_HEIGHT - block_y_len+1):
            for filed_x in range(FILED_WIDTH - block_x_len + 1):
                block_count = 0
                for idx, val in enumerate(arr):
                    # print(val[1], val[0])
                    if FILED[filed_x + (val[0]- block_size[0])][filed_y + (val[1] - block_size[2])] == 0:
                        block_count += 1
                if block_count == len(arr):
                    overlap = True
        
        option.append(overlap)

    false_count = 0
    for block_bool in option:
        if not block_bool:
            false_count += 1
        if false_count == len(option):
            return False
    return True

def popup(thisList):
    popup_width = screen_width - 80
    popup_height = 330
    popup_y_pos = screen_height / 2 - popup_height / 1.7
    popup_x_pos = screen_width / 2 - popup_width / 2
    
    popup_font = pygame.font.Font(None, 55)
    popup_font2 = pygame.font.Font(None, 35)
    popup_font3 = pygame.font.Font(None, 25)

    pygame.draw.rect(screen, (255, 255, 255), (
        popup_x_pos, 
        popup_y_pos,
        popup_width, popup_height)
    )
    pygame.draw.rect(screen, (0, 0, 0), (
        popup_x_pos, 
        popup_y_pos,
        popup_width, popup_height), 3
    )

    for idx, block in enumerate(thisList):
        for y in range(len(block)): 
            for x in range(len(block[y])):
                color = 0
                if block[y][x] != 0:
                    color = COLOR[block[y][x] - 1]
                else:
                    continue
                    
                block_size, arr = size(thisList, idx)
                block_y_len = block_size[3] - block_size[2] + 1

                
                pygame.draw.rect(screen, color, (
                    35*x + idx*120 + 70,
                    35*y + popup_y_pos + ((35*(4 - block_y_len)) / 2 + 80), 
                    35, 35), 0
                )
                pygame.draw.rect(screen, (0, 0, 0), (
                    35*x + idx*120 + 70,
                    35*y + popup_y_pos + ((35*(4 - block_y_len)) / 2 + 80), 
                    35, 35), 1
                )
            

    popup_title = popup_font.render("Level Up!", True, (255, 0, 0))
    popup_content = popup_font2.render("These blocks were added.", True, (0, 0, 0))
    popup_content2 = popup_font3.render("Click anywhere", True, (128, 128, 128))
    popup_title_rect = popup_title.get_rect()
    popup_content_rect = popup_content.get_rect()
    popup_content_rect2 = popup_content2.get_rect()
    screen.blit(popup_title, (screen_width / 2 - popup_title_rect[2] / 2 , popup_y_pos + 20))
    screen.blit(popup_content, (screen_width / 2 - popup_content_rect[2] / 2 , popup_y_pos + (popup_height - 75)))
    screen.blit(popup_content2, (screen_width / 2 - popup_content_rect2[2] / 2 , popup_y_pos + (popup_height - 45)))

def fade(arr):
    score_write()
    for a in range(0, 30):
        for data in arr:
            fade = pygame.Surface((data[2], data[3]))
            fade.fill((255, 255, 255))
            fade.set_alpha(a)
            screen.blit(fade, (data[0], data[1]))
            pygame.draw.rect(screen, (0, 0, 0), (data[0], data[1], data[2], data[3]), 1)
            pygame.display.update()

def score_write():
    total_score = game_score_font.render("Score: %s" % (score), True, (0, 0, 0))
    screen.blit(total_score, (FILED_PIECE_SIZE/2, FILED_PIECE_SIZE/2))

    b_score = best_score_font.render("Best Score: %s" % (best_score), True, (0, 0, 0))
    screen.blit(b_score, (FILED_PIECE_SIZE/2, FILED_PIECE_SIZE/2 + 40))

    l_level = level_font.render("level: %s" % (level), True, (0, 0, 0))
    screen.blit(l_level, (screen_width - 100 ,FILED_PIECE_SIZE/2))


def set_line_del():
    line_y = []
    line_x = []
    for y in range(FILED_HEIGHT):
        y_count = 0
        x_count = 0
        for x in range(FILED_WIDTH):
            if FILED[y][x] != 0:
                y_count += 1

            if FILED[x][y] != 0:
                x_count += 1
            if x_count >= FILED_WIDTH:
                line_x.append(y)

        if y_count >= FILED_HEIGHT:
            line_y.append(y)

    return (line_x, line_y)

def line_del(line_x, line_y):
    if line_x != [] or line_y != []:
        arr = []
        for y in range(FILED_HEIGHT):
            for liy in line_y:
                if y == liy:
                    for x in range(FILED_HEIGHT):
                        arr.append((FILED_X_POS+FILED_PIECE_SIZE*y, FILED_Y_POS+FILED_PIECE_SIZE*x, FILED_PIECE_SIZE, FILED_PIECE_SIZE))
        for x in range(FILED_HEIGHT):
            for y in range(FILED_WIDTH):
                for lix in line_x:
                    if x == lix:
                        arr.append((FILED_X_POS+FILED_PIECE_SIZE*y, FILED_Y_POS+FILED_PIECE_SIZE*x, FILED_PIECE_SIZE, FILED_PIECE_SIZE))
        fade(arr)
        for y in range(FILED_HEIGHT):
            for liy in line_y:
                if y == liy:
                    for x in range(FILED_HEIGHT):
                        FILED[y] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for x in range(FILED_HEIGHT):
            for y in range(FILED_WIDTH):
                for lix in line_x:
                    if x == lix:
                        FILED[y][x] = 0

        result = len(line_x) + len(line_y)
        return result
    


# 게임 실행
set_filed()
set_block()

while running:
    dt = clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_result = "QUIT"
            running = False

    # 마우스 이벤트
    if event.type == pygame.MOUSEBUTTONDOWN:
        if popup_on:
            popup_on = False

        if count == 0:
            start_to_x = pygame.mouse.get_pos()[0]
            start_to_y = pygame.mouse.get_pos()[1]
        md = True
        
        for block in block_list:
            block.rect.left = block.xpos
            block.rect.top = block.ypos
            if block.rect.collidepoint(event.pos):
                # 마우스를 클릭한 사각형 안에서의 x, y값
                block_cor = (event.pos[0] - block.xpos, event.pos[1] - block.ypos)
                click_block_list = block.list
                block_id = block.id
                block_num = block.num
                block_color = blocks[block_num][click_block_list[1]][click_block_list[0]]



    if event.type == pygame.MOUSEMOTION:
        if count >= 1:
            mouse_to_x = pygame.mouse.get_pos()[0] - start_to_x
            mouse_to_y = pygame.mouse.get_pos()[1] - start_to_y

    if md and event.type == pygame.MOUSEBUTTONUP:
        # print(block_color)
        # 블럭의 위치 정보
        borad_rect = Rect(FILED_X_POS, FILED_Y_POS, FILED_PIECE_SIZE*10, FILED_PIECE_SIZE*10)
            
        # 블럭을 클릭하거나 게임판을 클릭 했을때만 실행
        if block_cor != 0 or borad_rect.collidepoint(event.pos):
            # 만약 게임판을 처음으로 클릭한거면 count는 안 올라감
            if borad_rect.collidepoint(event.pos) and count == 0:
                count = 0
            else:
                count += 1

        if count >= 2 and block_cor != 0:
            # 게임판 기준으로 현재 마우스의 위치
            blo = cordinates(pygame.mouse.get_pos()[0] - FILED_X_POS, pygame.mouse.get_pos()[1] - FILED_Y_POS)
            block_x = blo[0]
            block_y = blo[1]

            # min_x, max_x, min_y, max_y
            if block_num != 100:
                block_size, arr = size(blocks, block_num)

            if click_block_list != 0 and block_x <= FILED_HEIGHT - 1 and block_y <= FILED_HEIGHT - 1 and block_x >= 0 and block_y >= 0:
                # 게임판에 그릴 도형의 시작 위치

                #       현재 마우스    블럭의 사각형위치   블럭의 시작위치
                start_x = block_x - click_block_list[0] + block_size[0]
                start_y = block_y - click_block_list[1] + block_size[2]

                # 게임판에 그릴 도형의 끝 위치
                last_x = start_x + (block_size[1] - block_size[0])
                last_y = start_y + (block_size[3] - block_size[2])

                if block_num != 100 and start_x >= 0 and start_y >= 0 and last_x <= FILED_HEIGHT - 1 and last_y <= FILED_HEIGHT - 1:
                    overlapping = False
                    filed_piece_list = []
                    for y in range((last_y - start_y) + 1):
                        for x in range((last_x - start_x) + 1):
                            if blocks[block_num][block_size[2] + y][block_size[0] + x] == 0:
                                continue
                            if FILED[start_x + x][start_y + y] != 0:
                                overlapping = True
                                filed_piece_list.clear()
                                break
                            filed_piece_list.append((start_x + x, start_y + y))
                        else:
                            continue
                        break

                    if not overlapping:
                        for filed in filed_piece_list:
                            FILED[filed[0]][filed[1]] = block_color
                            
                        for block in block_list:
                            if block.id == block_id:
                                del block
                        for idx, val in enumerate(random_block):
                            if idx == block_id:
                                random_block[idx] = 0
            
            # 값 초기화
            count = 0
            mouse_to_x = 0
            mouse_to_y = 0
            block_cor = 0
            rest_cor = 0
            start_to_x = 0
            start_to_y = 0
            block_id = 100
            block_num = 100
            click_block = 0
            click_block_list = 0
            block_color = 100
        md = False
        mu = True
    
    # 배경색 칠하기
    screen.fill(WHITE)
    screen.blit(logo, (logo_xpos, logo_ypos))


    # 도형 3개를 다 쓰면 다시 도형 만드는 함수
    random_filed = []
    for i in range(block_len):
        random_filed.append(0)
    if random_block == random_filed:
        random_block.clear()  
        block_list.clear()
        set_block()
    

    # 게임판이랑 도형 그리기 
    draw_filed()
    draw_filed2()       # 게임판 위에 테두리만 있는 게임판 1개를 더 그려 테투리 만들기
    draw_block()
    draw_block2()       # 블럭 위에 테두리만 있는 똑같은 블럭 1개를 더 그려 테투리 만들기

    lines = set_line_del()
    line_len = line_del(lines[0], lines[1])
    
    if line_len != None:
        if line_len == 1:
            score += 10
        elif line_len == 2:
            score += 25
        elif line_len == 3:
            score += 45
        elif line_len >= 4:
            score += 60
        
    if mu:
        running = gameover()
        mu = False


    if score >= 50 and level_up == 0:
        level = 2
        blocks += level2
        popup_on = True
        level_up += 1
    elif score >= 150 and level_up == 1:
        level = 3   
        popup_on = True
        blocks += level3
        level_up += 1
    elif score >= 250 and level_up == 2:
        level = 4
        popup_on = True
        blocks += level4
        level_up += 1
    elif score >= 400 and level_up == 3:
        level = 5
        popup_on = True
        blocks += level5
        level_up += 1

    if level == 2 and popup_on:
        popup(level2)
        pygame.time.delay(5)
    elif level == 3 and popup_on:
        popup(level3)
        pygame.time.delay(5)
    elif level == 4 and popup_on:
        popup(level4)
        pygame.time.delay(5)
    elif level == 5 and popup_on:
        popup(level5)
        pygame.time.delay(5)

    # 현재 점수 나타내기
    score_write()


    pygame.display.update()

# 게임 오버 메세지
msg = game_over_font.render(game_result, True, (255, 0, 0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2 - 60)))
screen.blit(msg, msg_rect)
pygame.display.update()

# 2초 대기
pygame.time.delay(2000)

print("게임 오버!")
if score > best_score:
    print("최고 점수 달성!!")
print("총 점수: ", score)


with open("C:/Users/User/Desktop/1010_game/js/record.json") as json_file:
    json_data = json.load(json_file)
    score_obj = json_data["score"]

    score_arr = []
    score_arr.extend(score_obj)
    if score != 0:
        score_arr.append(score)

    sc_obj = dict()
    sc_obj["score"] = score_arr
    
    with open("C:/Users/User/Desktop/1010_game/js/record.json", 'w', encoding='utf-8') as make_file:
        json.dump(sc_obj, make_file, indent="\t")
        

pygame.quit()

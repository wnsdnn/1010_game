import pygame
import random
import math

pygame.init()

# 전역 변수들
screen_width = 600
screen_height = 790
screen = pygame.display.set_mode((screen_width, screen_height)) 
screen_rect = screen.get_rect()

game_font = pygame.font.Font(None, 40)
game_over_font = pygame.font.Font(None, 80)

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
FILED_Y_POS = FILED_PIECE_SIZE * 2.2
# 도형들의 y좌표
block_y_pos = screen_height - 300
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

# 도형들의 인덱스 번호와 모양 정보가 있는 변수들
block_id = 100
block_num = 100

# 클릭한 도형의 사각형 인덱스 값
click_block_list = 0

game_result = "Game Over"

GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 도형들의 모양들
blocks = (
    # 0번째는 아무것도 없음(도형을 사용해도 안 밀리도록 도형 사용시 0번째 지정)
    ((0, 0, 0, 0),     
     (0, 0, 0, 0),    # 0
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 0, 1, 0),     
     (0, 0, 1, 0),    # 1
     (1, 1, 1, 0),
     (0, 0, 0, 0)),    
    ((0, 0, 0, 0),
     (0, 0, 0, 0),    # 2
     (0, 0, 0, 0),    
     (1, 1, 1, 1)),
    ((1, 1, 1, 0),    
     (1, 1, 1, 0),    # 3
     (1, 1, 1, 0),    
     (0, 0, 0, 0)),
    ((1, 1, 1, 0),
     (0, 0, 1, 0),    # 4
     (0, 0, 1, 0),    
     (0, 0, 0, 0)),
    ((1, 0, 0, 0),
     (1, 0, 0, 0),    # 5
     (1, 0, 0, 0),    
     (1, 1, 1, 0),
     (0, 0, 0, 0)),    
    ((0, 1, 0, 0),
     (0, 1, 0, 0),    # 6
     (0, 1, 0, 0),    
     (0, 1, 0, 0)),
    ((0, 0, 0, 0),
     (0, 0, 0, 0),    # 7
     (0, 0, 0, 0),    
     (0, 1, 1, 0)),
    ((0, 0, 0, 0),
     (0, 0, 0, 0),    # 8
     (0, 0, 0, 0),    
     (0, 1, 0, 0)),
    ((0, 1, 0, 0),
     (0, 1, 0, 0),    # 9
     (0, 1, 0, 0),    
     (0, 1, 0, 0)),
    ((0, 1, 1, 0),
     (0, 1, 0, 0),    # 10
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 1, 1, 0),
     (0, 0, 1, 0),    # 11
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((1, 1, 1, 0),
     (0, 1, 0, 0),    # 12
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 1, 0, 0),
     (1, 1, 1, 0),    # 13
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 1, 0, 0),
     (0, 1, 0, 0),    # 14
     (1, 1, 0, 0),
     (0, 0, 0, 0)),    
    ((0, 1, 0, 0),
     (0, 1, 0, 0),    # 15
     (0, 1, 1, 0),    
     (0, 0, 0, 0)),
    ((0, 1, 1, 0),
     (0, 1, 1, 0),    # 16
     (0, 0, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 1, 1, 0),
     (0, 0, 1, 0),    # 17
     (0, 0, 1, 0),    
     (0, 0, 0, 0)),
    ((0, 1, 1, 0),
     (0, 1, 0, 0),    # 18
     (0, 1, 0, 0),    
     (0, 0, 0, 0)),
    ((0, 0, 1, 0),
     (0, 1, 1, 0),    # 19
     (0, 0, 1, 0),    
     (0, 0, 0, 0)),
    ((0, 1, 0, 0),
     (0, 1, 1, 0),    # 20
     (0, 1, 0, 0),    
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

    def draw_borad(self):
        block = pygame.draw.rect(screen, (0, 0, 0), (self.xpos, self.ypos, FILED_PIECE_SIZE, FILED_PIECE_SIZE), self.line)
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

    def draw_block(self, mouse_xpos, mouse_ypos, id, color):
        xpos = 0
        ypos = 0
        if self.id == id:
            xpos = mouse_xpos
            ypos = mouse_ypos
        block = pygame.draw.rect(screen, color, (self.xpos + xpos, self.ypos + ypos, FILED_PIECE_SIZE, FILED_PIECE_SIZE))
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
            line_width = 1
            
            # 해당 값이 0이 아니라면 검은색으로 색칠
            if val != 0:
                line_width = 0
            borad = Borad(FILED_X_POS + y*FILED_PIECE_SIZE, FILED_Y_POS + x*FILED_PIECE_SIZE, line_width)
            borad_rect = borad.draw_borad()
            borad.get_rect(borad_rect)
            borad_list.append(borad)
            

# 게임에 사용할 도형 3개 배열에 넣는 함수
def set_block():
    for i in range(block_len):
        random_block.append(random.randrange(1, len(blocks)))
        # random_block.append(4)


# 도형을 그려 넣는 함수
def draw_block():
    for idx, val in enumerate(tuple(random_block)):
        for y in range(block_height):
            for x in range(block_width):
                if blocks[val][y][x] == 0:
                    continue
                block = Block(
                    FILED_PIECE_SIZE*x + idx*(FILED_PIECE_SIZE*3.5) + 70, 
                    FILED_PIECE_SIZE*y + block_y_pos + (FILED_PIECE_SIZE*block_height / 2), 
                    idx, val, (x, y))
                color = GRAY
                if count == 1 and block.id == block_id:
                    color = BLACK
                block_rect = block.draw_block(mouse_to_x, mouse_to_y, block_id, color)
                block.get_rect(block_rect)
                block_list.append(block)


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

def size(num):
    block_result = []
    for y in range(len(blocks[num])):
        for x in range(len(blocks[num][y])):
            if blocks[num][y][x] == 1:
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

############################### 오류 남 ######################################
def gameover():
    option = []
    for idx, random_num in enumerate(random_block):
        if random_num == 0:
            continue
        block_size, arr = size(random_num)
        block_y_len = block_size[3] - block_size[2] + 1
        block_x_len = block_size[1] - block_size[0] + 1
        
        # print(FILED_HEIGHT - block_y_len)
        # print(FILED_WIDTH - block_x_len)
        # for idx, val in enumerate(arr):
        #     print(val[1]- block_size[2], val[0] - block_size[0])
        # print(block_size)
        # return False
        overlap = False
        for filed_y in range(FILED_HEIGHT - block_y_len):
            for filed_x in range(FILED_WIDTH - block_x_len):
                block_count = 0
                for idx, val in enumerate(arr):
                    if FILED[filed_y + (val[1]- block_size[2])][filed_x + (val[0] - block_size[0])] == 0:
                        block_count += 1
                # print(overlap)
                if block_count == len(arr):
                    overlap = True
                # print(block_count, len(arr))

        option.append(overlap)
    # print(option)

    for block_bool in option:
        false_count = 0
        if not block_bool:
            false_count += 1
        if false_count == len(option):
            return False
    return True


# 게임 실행
set_filed()
set_block()

while running:
    dt = clock.tick(60)
    running = gameover()
    # gameover()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_result = "QUIT"
            running = False

    # 마우스 이벤트
    if event.type == pygame.MOUSEBUTTONDOWN:
        if count == 0:
            start_to_x = pygame.mouse.get_pos()[0]
            start_to_y = pygame.mouse.get_pos()[1]
        md = True

        for borad in borad_list:
            if borad.rect.collidepoint(event.pos):
                if count == 0:
                    md = False

        for block in block_list:
            block.rect.left = block.xpos
            block.rect.top = block.ypos
            if block.rect.collidepoint(event.pos):
                block_cor = (event.pos[0] - block.xpos, event.pos[1] - block.ypos)
                click_block_list = block.list
                block_id = block.id
                block_num = block.num


    if event.type == pygame.MOUSEMOTION:
        if count >= 1:
            mouse_to_x = pygame.mouse.get_pos()[0] - start_to_x
            mouse_to_y = pygame.mouse.get_pos()[1] - start_to_y


    if md and event.type == pygame.MOUSEBUTTONUP:
        count += 1

        if count >= 2 and block_cor != 0:
            # 게임판 기준으로 현재 마우스의 위치
            blo = cordinates(pygame.mouse.get_pos()[0] - FILED_X_POS, pygame.mouse.get_pos()[1] - FILED_Y_POS)
            block_x = blo[0]
            block_y = blo[1]

            # min_x, max_x, min_y, max_y
            if block_num != 100:
                block_size, arr = size(block_num)

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
                            if FILED[start_x + x][start_y + y] == 1:
                                overlapping = True
                                filed_piece_list.clear()
                                break
                            filed_piece_list.append((start_x + x, start_y + y))
                        else:
                            continue
                        break

                    if not overlapping:
                        for filed in filed_piece_list:
                            FILED[filed[0]][filed[1]] = 1
                            
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
        md = False
    
    # 배경색 칠하기
    screen.fill((255, 255, 255))
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
    draw_block()

    # 한줄 채워지면 삭제
    for y in range(FILED_HEIGHT):
        yy = 0
        xx = 0
        for x in range(FILED_WIDTH):
            if FILED[y][x] == 1:
                yy += 1

            if FILED[x][y] == 1:
                xx += 1
                if xx >= FILED_WIDTH:
                    for x in range(FILED_WIDTH):
                        FILED[x][y] = 0
                    score += 10

        if yy >= FILED_HEIGHT:
            FILED[y] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            score += 10

    # 현재 점수 나타내기
    total_score = game_font.render("Score: %s" % (score), True, (0, 0, 0))
    screen.blit(total_score, (FILED_PIECE_SIZE/2, FILED_PIECE_SIZE/2))

    

    # running = False
    pygame.display.update()

    
# 게임 오버 메세지

msg = game_over_font.render(game_result, True, (255, 0, 0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2 - 60)))
screen.blit(msg, msg_rect)
pygame.display.update()

# 2초 대기
pygame.time.delay(2000)

pygame.quit()

#  남은일 
#  1. 게임 오버 기능 구현
#  2. 마우스 이벤트 오류 안나게 고치기
#  3. 게임 플레이나 기능구현시 나오는 오류 수정
#  4. 디자인 예쁘게 수정하기
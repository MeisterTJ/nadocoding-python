import os
import pygame

##############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640  # 가로 크기
screen_height = 480  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Pang")

# FPS
clock = pygame.time.Clock()

# 누르고 있을 경우 반복 입력되도록 한다.
pygame.key.set_repeat(1, 1)
##############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")  # current_path + images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 0.5

# 무기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_pressed = False

# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 1

# 공 만들기 (4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

# 공 크기에 따른 속도
ball_speeds_y = [-1.0, -0.9, -0.6, -0.3]

# 공들을 관리하는 리스트, 최초 발생하는 큰 공 추가
balls = [{
    "pos_x": 50,
    "pos_y": 50,
    "img_idx": 0,
    "to_x": 0.2,
    "to_y": -0.6,
    "init_speed_y": ball_speeds_y[0]  # y축 최초 속도 (공마다 다르니깐)
}]

running = True
while running:
    dt = clock.tick(60)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # 플레이어를 왼쪽으로 이동한다.
                character_to_x = -character_speed
            elif event.key == pygame.K_RIGHT:  # 플레이어를 오른쪽으로
                character_to_x = character_speed
            elif event.key == pygame.K_SPACE and weapon_pressed is False:  # 무기 발사
                weapon_pressed = True
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])  # 무기 리스트에 추가한다.

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
            if event.key == pygame.K_SPACE:
                weapon_pressed = False

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정, 무기 위치를 계속해서 위로 올린다.
    # w의 각각의 위치를 수정해서 다시 list로 전달한다.
    weapons = [[w[0], w[1] - weapon_speed * dt] for w in weapons]

    # 천장에 닿은 무기 없애기
    # w[1] > 0이 충족되는 것들만 리스트로 보낸다.
    weapons = [[w[0], w[1]] for w in weapons if w[1] >= 0]

    # 공 위치 정의
    # ball_idx는 리스트에서의 인덱스, ball_val은 실제 dict
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 공이 가로벽에 닿았을 때 공 이동 방향 변경
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        # 세로 위치
        # 스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_speed_y"]
        else:   # 중력 제어
            ball_val["to_y"] += 0.0025 * dt

        ball_val["pos_x"] += ball_val["to_x"] * dt
        ball_val["pos_y"] += ball_val["to_y"] * dt

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()

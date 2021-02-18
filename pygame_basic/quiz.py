import random
import pygame

pygame.init()
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Quiz")

# FPS 설정
clock = pygame.time.Clock()

# 누르고 있을 경우 반복 입력되도록 한다.
pygame.key.set_repeat(1, 1)

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/chogdak/PycharmProjects/nadocoding/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size  # 튜플로 가로, 세로 크기 가져오기
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - character_width / 2  # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 똥 만들기
enemy = pygame.image.load("enemy.png")
enemy_size = enemy.get_rect().size  # 튜플로 가로, 세로 크기 가져오기
enemy_width = enemy_size[0]  # 캐릭터의 가로 크기
enemy_height = enemy_size[1]  # 캐릭터의 세로 크기
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 1.5

# 이동할 좌표
to_x = 0

# 이동 속도
character_speed = 0.6

# 매 프레임 당 호출되는 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(60)  # 초당 60프레임으로 돌리고 싶다.

    for event in pygame.event.get():  # 키보드나 마우스 입력이 들어오는지 체크한다.
        if event.type == pygame.QUIT:  # x 버튼을 누를시 발생
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x = -character_speed
            elif event.key == pygame.K_RIGHT:
                to_x = character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += (to_x * dt)

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed * dt

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False


    # 화면에 그리기
    screen.blit(background, (0, 0))  # 0,0 위치에 background 를 그린다.
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 똥 그리기

    pygame.display.update()  # 게임 화면을 다시 그려준다.

# 게임 종료
pygame.quit()
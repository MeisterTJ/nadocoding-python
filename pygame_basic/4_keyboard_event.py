import pygame

pygame.init()   # pygame을 초기화하는 작업 (반드시 필요)

# 화면 크기 설정
screen_width = 480   # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")     # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/chogdak/PycharmProjects/nadocoding/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size      # 튜플로 가로, 세로 크기 가져오기
character_width = character_size[0]             # 캐릭터의 가로 크기
character_height = character_size[1]            # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - character_width / 2   # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height         # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 매 프레임 당 호출되는 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():    # 키보드나 마우스 입력이 들어오는지 체크한다.
        if event.type == pygame.QUIT:   # x 버튼을 누를시 발생
            running = False             # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:    # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:      # character to leftward
                to_x -= 5
            elif event.key == pygame.K_RIGHT:   # character to rightward
                to_x += 5
            elif event.key == pygame.K_UP:      # character to upward
                to_y -= 5
            elif event.key == pygame.K_DOWN:    # character to downward
                to_y += 5

        if event.type == pygame.KEYUP:      # 키를 뗐을 경우
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # screen.fill((0, 0, 255))            # 색을 채우는 방법
    screen.blit(background, (0, 0))     # 0,0 위치에 background 를 그린다.
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()     # 게임 화면을 다시 그려준다.

# 게임 종료
pygame.quit()
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

# 매 프레임 당 호출되는 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():    # 키보드나 마우스 입력이 들어오는지 체크한다.
        if event.type == pygame.QUIT:   # x 버튼을 누를시 발생
            running = False             # 게임이 진행중이 아님

    # screen.fill((0, 0, 255))            # 색을 채우는 방법
    screen.blit(background, (0, 0))     # 0,0 위치에 background 를 그린다.
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()     # 게임 화면을 다시 그려준다.

# 게임 종료
pygame.quit()
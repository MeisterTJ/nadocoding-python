import pygame

pygame.init()   # pygame을 초기화하는 작업 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")     # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/chogdak/PycharmProjects/nadocoding/pygame_basic/background.png")

# 매 프레임 당 호출되는 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():    # 키보드나 마우스 입력이 들어오는지 체크한다.
        if event.type == pygame.QUIT:   # x버튼을 누를시 발생
            running = False             # 게임이 진행중이 아님

    # screen.fill((0, 0, 255))            # 색을 채우는 방법
    screen.blit(background, (0, 0))     # 0,0 위치에 background를 그린다.
    pygame.display.update()     # 게임 화면을 다시 그려준다.

# 게임 종료
pygame.quit()
import pygame

pygame.init()   # pygame을 초기화하는 작업 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")     # 게임 이름

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():    # 키보드나 마우스 입력이 들어오는지 체크한다.
        if event.type == pygame.QUIT:   # x버튼을 누를시 발생
            running = False             # 게임이 진행중이 아님


# 게임 종료
pygame.quit()
import pygame

# 초기화 ( 그냥 반드시 필요 )
pygame.init() 

# 화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 타이틀 설정
pygame.display.set_caption("test game") # 게임 이름

# 이벤트 루프

switch = True # 게임이 진행중인가?
while switch:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 오른쪽위에 창을 끄는  이벤트가 발생하였으면?
            switch = False # 게임이 진행중이 아님


# pygame 종료
pygame.quit()

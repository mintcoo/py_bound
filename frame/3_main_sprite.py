import pygame

# 초기화 ( 그냥 반드시 필요 )
pygame.init() 

# 화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 타이틀 설정
pygame.display.set_caption("test game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\xhakt\\Desktop\\mini_pjt\\py_practice_pygame\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\xhakt\\Desktop\\mini_pjt\\py_practice_pygame\\character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) 
# 화면 가로 크기의 절반에 해당하는 곳에 위치하기 위해 좌표를 중앙에서 캐릭터 크기의 절반만큼 옮겨와야함

character_y_pos = screen_height - character_height # 화면 세로크기 - 캐릭터의 크기
# 캐릭터 위치도 좌표값으로 해서 나타내어주니까 계산을 잘해야함


# 이벤트 루프

switch = True # 게임이 진행중인가?
while switch:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 오른쪽위에 창을 끄는  이벤트가 발생하였으면?
            switch = False # 게임이 진행중이 아님

    screen.blit(background, (0, 0)) # 배경 그리기 (좌표 0, 0 이 제일왼쪽위)
    
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update() # 게임화면을 다시 그리기! (while 동안 계쏙 돌면서 화면을 다시 그림 필수임!)




# pygame 종료
pygame.quit()

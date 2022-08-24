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


# 이동할 좌표
to_x = 0
to_y = 0


# 이벤트 루프

switch = True # 게임이 진행중인가?
while switch:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 오른쪽위에 창을 끄는  이벤트가 발생하였으면?
            switch = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= 0.1 
            elif event.key == pygame.K_RIGHT : # 캐릭터를 오른쪽으로
                to_x += 0.1
            elif event.key == pygame.K_UP : # 캐릭터를 위로
                to_y -= 0.1
            elif event.key == pygame.K_DOWN : # 캐릭터를 아래로
                to_y += 0.1

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x
    character_y_pos += to_y
    # 여기서 이제 캐릭터 그려지는 좌표값에 key를 입력하는 만큼 값이 더해지거나 빼짐

    # 가로 경계값 처리
    if character_x_pos < 0: 
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # ★캐릭터 크기만큼 빼줘야 끝에 그려진다!
            character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0: 
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0)) # 배경 그리기 (좌표 0, 0 이 제일왼쪽위)
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 계속 캐릭터를 그림
    
    pygame.display.update() # 게임화면을 다시 그리기! (while 동안 계쏙 돌면서 화면을 다시 그림 필수임!)




# pygame 종료
pygame.quit()

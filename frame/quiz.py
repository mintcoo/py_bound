import pygame
import random
#################################################################
# 기본 초기화 (반드시 해야 하는 것들)
# 초기화 ( 그냥 반드시 필요 )
pygame.init() 

# 화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 타이틀 설정
pygame.display.set_caption("poop") # 게임 이름

# FPS
clock = pygame.time.Clock()
#################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경
background = pygame.image.load("C:\\Users\\xhakt\\Desktop\\mini_pjt\\py_practice_pygame\\background.png") 

# 캐릭터
character = pygame.image.load("C:\\Users\\xhakt\\Desktop\\mini_pjt\\py_practice_pygame\\character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height 

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 1


# 적 enemy 캐릭터
enemy = pygame.image.load("C:\\Users\\xhakt\\Desktop\\mini_pjt\\py_practice_pygame\\enemy.png")
enemy_size = enemy.get_rect().size # 이미지 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = random.randrange(0, (screen_width - enemy_width))
enemy_y_pos = 0
enemy_speed = 10



# 이벤트 루프
switch = True # 게임이 진행중인가?
while switch:
    dt = clock.tick(30) # 게임화면의 초당 프레임수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 오른쪽위에 창을 끄는  이벤트가 발생하였으면?
            switch = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT : # 캐릭터를 오른쪽으로
                to_x += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randrange(0, (screen_width - enemy_width))
        enemy_y_pos = 0
    

    character_x_pos += to_x *dt
    enemy_y_pos += enemy_speed


    # 3. 게임 캐릭터 위치 정의

    # 가로 경계값 처리
    if character_x_pos < 0: 
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # ★캐릭터 크기만큼 빼줘야 끝에 그려진다!
            character_x_pos = screen_width - character_width



    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌함")
        switch = False


    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기 (좌표 0, 0 이 제일왼쪽위)
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 계속 캐릭터를 그림
    
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    pygame.display.update() # 게임화면을 다시 그리기! (while 동안 계쏙 돌면서 화면을 다시 그림 필수임!)

pygame.time.delay(2000) # 2초 정도 대기 (ms)

# pygame 종료
pygame.quit()

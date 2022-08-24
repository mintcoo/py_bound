import pygame

# 초기화 ( 그냥 반드시 필요 )
pygame.init() 

# 화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 타이틀 설정
pygame.display.set_caption("test game") # 게임 이름

# FPS
clock = pygame.time.Clock()


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

# 이동 속도
character_speed = 0.5

# 적 enemy 캐릭터
enemy = pygame.image.load("C:\\Users\\xhakt\\Desktop\\mini_pjt\\py_practice_pygame\\enemy.png")
enemy_size = enemy.get_rect().size # 이미지 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) 
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) 

# 폰트 정의
game_font = pygame.font.Font(None, 30) # 폰트 객체 생성 (폰트, 크기)


# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴


# 이벤트 루프
switch = True # 게임이 진행중인가?
while switch:
    dt = clock.tick(60) # 게임화면의 초당 프레임수를 설정

# 캐릭터가 1초동안에 100만큼 이동을 해야함
# 10 fpx : 1초동안에 10번 동작 -> 한번에 10만큼 이동함 10 * 10 = 100
# 20 fps : 1초동안에 20번 동작 -> 한번에 5만큼 이동 5 * 20 = 100


    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 오른쪽위에 창을 끄는  이벤트가 발생하였으면?
            switch = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT : # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP : # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN : # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x *dt
    character_y_pos += to_y *dt
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

    


    screen.blit(background, (0, 0)) # 배경 그리기 (좌표 0, 0 이 제일왼쪽위)
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 계속 캐릭터를 그림
    
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    # 밀리세컨드라(ms) 환산하기 위해서 1000으로 나누어서 초(s) 단위로 표시
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255 ))

    # 소수점 안나오고 깔끔하게 초단위로 계산위해 int로 감싸고 render뒤에는 문자로, 다시 str로 감쌈
    # 출력할 글자, True(무조건), 글자 색상

    # text = game_font.render((f'Life : {int(total_time - elapsed_time)}'), True, (255, 255, 255))

    screen.blit(timer, (10, 10))
    # screen.blit(text, (10, 50))
    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        switch = False

    pygame.display.update() # 게임화면을 다시 그리기! (while 동안 계쏙 돌면서 화면을 다시 그림 필수임!)

# 잠시 대기 (종료전에)
pygame.time.delay(2000) # 2초 정도 대기 (ms)


# pygame 종료
pygame.quit()

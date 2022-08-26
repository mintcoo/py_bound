import os

import pygame

from src.prefabs.Application import Application
from src.prefabs.PatternMaker import PatternMaker
from src.prefabs.Stage import Stage
from src.utils.util import format_time


def run(size):
    app = Application(size=size, fps=60, title="Bound")
    RESOURCES = app.RESOURCES
    screen = app.screen

    # 배경음악 설정
    sound = pygame.mixer.Sound("resources/music/summer.mp3")
    sound.set_volume(0.4)
    sound.play(-1)

    # FPS
    clock = pygame.time.Clock()
    #################################################################

    # 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
    current_path = os.path.dirname(os.curdir)  # 현재 파일의 위치를 반환

    # 캐릭터 만들기
    character = RESOURCES["IMAGE"]["poong.png"]
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = 150
    character_y_pos = 100

    # 캐릭터 스피드
    character_speed = 0.1

    # 캐릭터 이동 좌표
    to_x = 0
    to_y = 0

    # 캐릭터 움직임 스위치
    move_switch_R = False
    move_switch_L = False
    move_switch_U = False
    move_switch_D = False

    # 마우스 커서 만들기
    mouse = RESOURCES["IMAGE"]["mouse.png"]
    mouse_size = mouse.get_rect().size
    mouse_width = mouse_size[0]
    mouse_height = mouse_size[1]

    # 마우스 위치
    mouse_position = (0, 0)

    # 마우스 스위치
    mouse_draw = False

    # 폰트 정의
    game_font = pygame.font.Font(None, 30)  # 폰트 객체 생성 (폰트, 크기)
    pattern_maker = PatternMaker(app)

    # 폭탄 초기화
    patterns = pattern_maker.create()
    stage = Stage(patterns, app)
    # 시작 시간 정보
    start_ticks = pygame.time.get_ticks()  # 시작 tick을 받아옴

    # 이벤트 루프
    switch = True  # 게임이 진행중인가?
    while switch:
        delta_time = clock.tick(60)  # 게임화면의 초당 프레임수를 설정

        # 2. 이벤트 처리 (키보드, 마우스 등)
        for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:  # 오른쪽위에 창을 끄는  이벤트가 발생하였으면?
                switch = False  # 게임이 진행중이 아님

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    mouse_position = pygame.mouse.get_pos()
                    mouse_draw = True
                    move_switch_R = False
                    move_switch_L = False
                    move_switch_U = False
                    move_switch_D = False
                    to_x = 0
                    to_y = 0
                    # print(mouse_position)
                    left_right = abs(mouse_position[0] - character_x_pos)
                    up_down = abs(mouse_position[1] - character_y_pos)

                    # 우상향
                    if (
                            mouse_position[0] > character_x_pos
                            and mouse_position[1] < character_y_pos
                    ):
                        move_switch_R = True
                        move_switch_U = True
                        if left_right > up_down:
                            to_x += character_speed
                            to_y -= character_speed * up_down / left_right

                        elif left_right == up_down:
                            to_x += character_speed
                            to_y -= character_speed
                        elif left_right < up_down:
                            to_x += character_speed * left_right / up_down
                            to_y -= character_speed

                    # 우하향
                    if (
                            mouse_position[0] > character_x_pos
                            and mouse_position[1] > character_y_pos
                    ):
                        move_switch_R = True
                        move_switch_D = True
                        if left_right > up_down:
                            to_x += character_speed
                            to_y += character_speed * up_down / left_right

                        elif left_right == up_down:
                            to_x += character_speed
                            to_y += character_speed

                        elif left_right < up_down:
                            to_x += character_speed * left_right / up_down
                            to_y += character_speed

                    # 좌상향
                    if (
                            mouse_position[0] < character_x_pos
                            and mouse_position[1] < character_y_pos
                    ):
                        move_switch_L = True
                        move_switch_U = True
                        if left_right > up_down:
                            to_x -= character_speed
                            to_y -= character_speed * up_down / left_right

                        elif left_right == up_down:
                            to_x -= character_speed
                            to_y -= character_speed
                        elif left_right < up_down:
                            to_x -= character_speed * left_right / up_down
                            to_y -= character_speed

                    # 좌하향
                    if (
                            mouse_position[0] < character_x_pos
                            and mouse_position[1] > character_y_pos
                    ):
                        move_switch_L = True
                        move_switch_D = True
                        if left_right > up_down:
                            to_x -= character_speed
                            to_y += character_speed * up_down / left_right

                        elif left_right == up_down:
                            to_x -= character_speed
                            to_y += character_speed

                        elif left_right < up_down:
                            to_x -= character_speed * left_right / up_down
                            to_y += character_speed

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    mouse_draw = False

        # 3. 게임 캐릭터와 마우스 처리

        # 가로 경계값 처리

        if character_x_pos < 120:
            character_x_pos = 120
        elif 395 < character_x_pos < 400 and 150 < character_y_pos < 200:
            character_x_pos = 395
        elif 395 < character_x_pos < 400 and 20 < character_y_pos < 50:
            character_x_pos = 395

        # 세로 경계값 처리
        if character_y_pos < 30:
            character_y_pos = 30
        elif character_y_pos > 180:
            character_y_pos = 180
        elif character_x_pos > 400 and 55 > character_y_pos:
            character_y_pos = 55
        elif character_x_pos > 400 and 145 < character_y_pos:
            character_y_pos = 145

        character_x_pos += to_x * delta_time
        character_y_pos += to_y * delta_time

        if move_switch_R == True and mouse_position[0] < character_x_pos:
            to_x = 0
            move_switch_R = False
        if move_switch_L == True and mouse_position[0] > character_x_pos:
            to_x = 0
            move_switch_L = False
        if move_switch_D == True and mouse_position[1] < character_y_pos:
            to_y = 0
            move_switch_D = False
        if move_switch_U == True and mouse_position[1] > character_y_pos:
            to_y = 0
            move_switch_U = False

        # 4. 충돌 처리

        # 충돌 처리를 위한 rect 정보 업데이트
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        # 5. 화면에 그리기
        background = RESOURCES["IMAGE"]["background.png"]
        zone = RESOURCES["IMAGE"]["zone.png"]
        stage_image = RESOURCES["IMAGE"]["stage.png"]
        screen.blit(background, (0, 0))
        screen.blit(zone, (100, 20))
        screen.blit(stage_image, (400, 50))

        # 시간 milliseconds
        elapsed_time = int((pygame.time.get_ticks() - start_ticks))

        timer = game_font.render(format_time(elapsed_time), True, (255, 255, 255))
        screen.blit(timer, (size[0] / 2 - timer.get_width() / 2, 0))

        stage.update(delta_time)

        if mouse_draw == True:
            screen.blit(
                mouse,
                (
                    mouse_position[0] - mouse_width / 2,
                    mouse_position[1] - mouse_height / 2,
                ),
            )

        screen.blit(
            character,
            (
                character_x_pos - character_width / 2,
                character_y_pos - character_height / 2,
            ),
        )

        # 충돌 체크
        if type(stage.current_pattern).__name__ == "list":
            character_rect = character.get_rect()
            character_rect.left = character_x_pos - character_width / 2
            character_rect.top = character_y_pos - character_height / 2
            for bomb in stage.current_pattern:
                if bomb.animation_index != 0:
                    continue
                bomb_rect = pygame.Rect(bomb.position, bomb.image.get_size())
                is_collision = character_rect.colliderect(bomb_rect)
                if is_collision:
                    character_x_pos = 30
                    character_y_pos = 30

        pygame.display.update()  # 게임화면을 다시 그리기! (while 동안 계쏙 돌면서 화면을 다시 그림 필수임!)

    # pygame 종료
    pygame.quit()

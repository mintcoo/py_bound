import os

import pygame

from src.prefabs.Application import Application
from src.prefabs.PatternMaker import PatternMaker
from src.prefabs.Player import Player
from src.prefabs.Stage import Stage
from src.utils.constants import M_RIGHT, FONT_PATH
from src.utils.util import format_time


def run(size):
    # 앱세팅
    app = Application(size=size, fps=60, title="Bound")
    RESOURCES = app.RESOURCES
    screen = app.screen
    game_font = pygame.font.Font(FONT_PATH, 30)  # 폰트 객체 생성 (폰트, 크기)
    start_ticks = pygame.time.get_ticks()  # 시작 tick을 받아옴
    clock = pygame.time.Clock()  # FPW

    # 배경음악 설정
    sound = pygame.mixer.Sound("resources/music/summer.mp3")
    sound.set_volume(0.4)
    sound.play(-1)

    # 이미지 리소스 로드 및 Rect 세팅
    background = RESOURCES["IMAGE"]["background.png"]
    zone = RESOURCES["IMAGE"]["zone.png"]
    stage_image = RESOURCES["IMAGE"]["stage.png"]
    zone_rect = pygame.Rect((100, 20), (zone.get_size()))
    stage_rect = pygame.Rect((400, 50), (stage_image.get_size()))

    ############################
    # Object 준비
    ############################

    # 캐릭터 생성
    character = Player(app)
    character.set_position((150, 100))

    # 못넘어가게 막는 벽 생성
    walls = []
    # pygame.Rect(zone)

    # 패턴 생성
    pattern_maker = PatternMaker(app)
    patterns = pattern_maker.create()
    stage = Stage(patterns, app)

    # 이벤트 루프
    app.is_running = True  # 게임이 진행중인가?
    while app.is_running:
        delta_time = clock.tick(app.fps)  # 게임화면의 초당 프레임수를 설정
        app.set_delta_time(delta_time)

        # 2. 이벤트 처리 (키보드, 마우스 등)
        for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:  # 오른쪽위에 창을 끄는  이벤트가 발생하였으면?
                app.is_running = False  # 게임이 진행중이 아님
            character.mouse.on_event(event)

        # 화면 업데이트
        screen.blit(background, (0, 0))
        screen.blit(zone, zone_rect)
        screen.blit(stage_image, stage_rect)

        # 오브젝트 업데이트
        character.update()
        stage.update(delta_time)

        # 타이머 업데이트
        elapsed_time = int((pygame.time.get_ticks() - start_ticks))
        timer = game_font.render(format_time(elapsed_time), True, (255, 255, 255))
        screen.blit(timer, (size[0] / 2 - timer.get_width() / 2, 0))

        # 충돌 체크
        if type(stage.current_pattern).__name__ == "list":
            character_rect = character.rect
            for bomb in stage.current_pattern:
                if bomb.animation_index != 0:
                    continue
                bomb_rect = pygame.Rect(bomb.position, bomb.image.get_size())
                is_collision = character_rect.colliderect(bomb_rect)
                if is_collision:
                    character.death()

        pygame.display.update()  # 게임화면을 다시 그리기! (while 동안 계쏙 돌면서 화면을 다시 그림 필수임!)

    # pygame 종료
    pygame.quit()

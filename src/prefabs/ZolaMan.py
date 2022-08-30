import pygame

from src.prefabs.GameObject import GameObject
from src.prefabs.ZolaManAttackAnimation import ZolaManAttackAnimation
from src.utils.spritesheet import SpriteSheet


class ZolaMan(GameObject):
    speed = 0.1
    offset = [0, 0]
    sprites_delay = 10
    sprites_delay_count = sprites_delay
    status = "neutral"
    base_attack_speed = 2000
    attack_speed = base_attack_speed
    attack_speed_delay_count = attack_speed
    animations = []
    multiple_attack_max_count = 5


    def get_attack_speed_per_percent(self, percent=10):
        as_per_one_percent = (self.base_attack_speed - 1000) / 100
        return as_per_one_percent * percent

    def __init__(self, app):
        self.app = app
        self.sprites = []
        self.set_status('neutral')
        self.size = self.image.get_rect().size

    def set_position(self, position):
        self.position = position
        self.rect = pygame.Rect(self.position, self.size)
        self.rect.left = self.position[0] - self.size[0] / 2
        self.rect.top = self.position[1] - self.size[1] / 2

    def set_status(self, status):
        app = self.app
        sheet = []
        idle_sheet = SpriteSheet(app.RESOURCES["IMAGE"]["zolaman/zola-idle.png"])
        attack_sheet = SpriteSheet(app.RESOURCES["IMAGE"]["zolaman/zola-attack.png"])
        if status == 'neutral':
            sheet = [
                idle_sheet.image_at((0, 0, 15, 30)),
                idle_sheet.image_at((15, 0, 15, 30)),
                idle_sheet.image_at((30, 0, 15, 30))
            ]

        if status == 'attack':
            sheet = [
                attack_sheet.image_at((0, 0, 20, 30)),
                attack_sheet.image_at((20, 0, 20, 30)),
                attack_sheet.image_at((40, 0, 20, 30))
            ]

        self.sprites = sheet

        self.sprites_delay_count = self.sprites_delay
        self.sheet_index = 0
        self.image = self.sprites[0]
        self.status = status

    def update_sprite(self):

        self.attack_speed_delay_count -= self.app.delta_time
        if self.attack_speed_delay_count <= 0:
            self.attack_speed_delay_count = self.attack_speed
            self.attack()

        self.sprites_delay_count -= 1
        if self.sprites_delay_count == 0:
            self.sheet_index += 1
            if self.sheet_index >= self.sprites.__len__():
                self.sheet_index = 0
                self.on_sprite_animation_end()
                pass
            self.image = self.sprites[self.sheet_index]
            self.sprites_delay_count = self.sprites_delay

        #
        if self.status == 'attack':
            self.weapon_attack_animation.update()

    def on_sprite_animation_end(self):
        if self.status == 'attack':
            self.set_status('neutral')

    def attack(self):
        self.set_status('attack')
        for animation in self.animations:
            animation.reset()

    def start(self):
        super().start()
        weapon_attack_sheet = SpriteSheet(self.app.RESOURCES["IMAGE"]["weapon/sword-attack.png"])
        self.weapon_attack_animation = ZolaManAttackAnimation(weapon_attack_sheet, self.app)
        self.weapon_attack_animation.set_target(self)
        self.weapon_attack_animation.set_sprites([
            (29 * 0, 0, 29, 36),
            (29 * 1, 0, 29, 36),
            (29 * 2, 0, 29, 36),
        ])
        self.weapon_attack_animation.set_position([self.position[0] - 9, self.position[1] - 20])
        self.animations.append(self.weapon_attack_animation)

    def on_collision_weapon(self, target):
        target.set_sheet('death')

    def update(self):
        screen = self.app.screen
        screen.blit(self.image, self.rect)
        self.update_sprite()

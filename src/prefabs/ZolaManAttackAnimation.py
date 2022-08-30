from src.prefabs.Animation import Animation


class ZolaManAttackAnimation(Animation):
    is_attacked = False
    target = None

    def __init__(self, sheet, app, delay=10):
        super().__init__(sheet, app, delay)

    def reset(self):
        super().reset()
        self.is_attacked = False

    def set_target(self, target):
        self.target = target

    def update(self):
        super().update()
        snails = list(filter(lambda object: object.__class__.__name__ == 'Snail', self.app.game_objects))
        [zolaman] = list(filter(lambda object: object.__class__.__name__ == 'ZolaMan', self.app.game_objects))

        if self.is_attacked is True:
            return

        attacked = 0
        for snail in snails:
            if snail.rect.colliderect(self.get_rect()):
                self.is_attacked = True
                self.target.on_collision_weapon(snail)
                attacked += 1
                print(zolaman.multiple_attack_max_count, attacked)
                if zolaman.multiple_attack_max_count <= attacked:
                    break

    def on_animation_end(self):
        self.is_attacked = False

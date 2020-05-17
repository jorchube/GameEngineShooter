from shooter import collision_masks
from shooter.bullets.bullet import Bullet, BigBullet


class BasicBullet(Bullet):
    def __init__(self):
        super().__init__()
        self.collision_mask = collision_masks.ENEMY_BULLET


class BigBullet(BigBullet):
    def __init__(self):
        super().__init__()
        self.collision_mask = collision_masks.ENEMY_BULLET
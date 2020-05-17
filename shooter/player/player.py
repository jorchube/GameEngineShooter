from game_engine.actor import PlayerActor
from game_engine.component import PolygonComponent, HitboxComponent
from game_engine.event import CollisionEvent
from game_engine.event.event_type import key_event
from game_engine.game import Game
from game_engine.geometry import Polygon, Point3D, Vector3D

from shooter import collision_masks
from shooter.bullets.bullet import Bullet
from shooter.effects.sound import SoundEffects


class Player(PlayerActor):
    def __init__(self):
        super().__init__()
        self.__shooting = False
        self.__create_body()
        self.__subscribe_to_events()
        self.collision_mask = collision_masks.ENEMY_BULLET
        self.position.x = -15
        self.position.y = 5
        self.__shoot_cooldown = 0.2
        self.__next_shoot_after = 0

    def __subscribe_to_events(self):
        self.subscribe_to_event(key_event.KeyEventPress, self.__on_key_press_event)
        self.subscribe_to_event(key_event.KeyEventRelease, self.__on_key_release_event)
        self.subscribe_to_event(CollisionEvent, self.__on_collision_event)

    def __create_body(self):
        body = Polygon([Point3D(0.5, 0, 0), Point3D(-0.5, 0.3, 0), Point3D(-0.5, -0.3, 0)])
        self.add_component(PolygonComponent(body))
        self.add_component(HitboxComponent(body, is_collision_source=True))

    def __on_key_press_event(self, event):
        if event.key == key_event.Key.space:
            self.__shooting = True

    def __on_key_release_event(self, event):
        if event.key == key_event.Key.space:
            self.__shooting = False

    def __on_collision_event(self, event):
        pass

    def __shoot(self):
        time = Game.running_time_seconds()
        if self.__next_shoot_after > time:
            return

        bullet = Bullet(2)
        bullet.collision_mask = collision_masks.PLAYER_BULLET
        bullet.position = self.position
        bullet.move_vector = Vector3D(30, 0, 0)
        Game.current_scene().add_actor(bullet)

        self.__next_shoot_after = time + self.__shoot_cooldown

    def end_tick(self):
        if self.__shooting:
            self.__shoot()
        super().end_tick()

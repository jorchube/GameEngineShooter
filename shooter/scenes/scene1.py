from game_engine.actor.fps_actor import FPSActor
from game_engine.game import Game
from game_engine.geometry import Point3D
from game_engine.scene.scene import Scene

from shooter.enemy_factory.enemy_body_hitbox_component_tuple_collection import EnemyBodyHitboxComponentTupleCollection
from shooter.enemy_factory.enemy_factory import EnemyFactory
from shooter.enemy_factory.move_component_collection import EnemyMoveComponentCollection
from shooter.enemy_factory.shoot_pattern_component_collection import EnemyShootPatternComponentCollection


class EnemyScheduling(object):
    def __init__(self, spawn_callback, delay_seconds):
        self.callback = spawn_callback
        self.delay_seconds = delay_seconds


class Scene1(Scene):
    def __init__(self, display):
        super().__init__(display)
        self.__add_fps_counter()
        self.__create_enemy_schedule()
        self.last_scheduled_time = 0

    def __add_fps_counter(self):
        fps = FPSActor()
        fps.position.x = 25
        fps.position.y = -20
        self.add_actor(fps)

    def __add_enemy(self, enemy_class, x, y):
        e = enemy_class()
        e.position = Point3D(x, y, 0)
        self.add_actor(e)

    def __create_enemy_schedule(self):
        self.enemy_schedule = \
            self.triangles_from_top() + \
            self.enemy_scheduling_stall(1) + \
            self.triangles_from_bottom() + \
            self.enemy_scheduling_stall(5) + \
            self.two_octogons_in_parallel() + \
            self.enemy_scheduling_stall(5) + \
                self.triangles_in_triangle_formation() + \
            [
                EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_big, 32, 0), 8),
            ]

    def end_tick(self):
        super().end_tick()
        self.__schedule_enemies()

    def __schedule_enemies(self):
        current_time = Game.running_time_seconds()
        while self.enemy_schedule and (current_time - self.last_scheduled_time) >= self.enemy_schedule[0].delay_seconds:
            self.enemy_schedule.pop(0).callback()
            self.last_scheduled_time = current_time

    def enemy_scheduling_stall(self, seconds):
        return [EnemyScheduling(lambda: None, seconds)]

    def triangles_from_top(self):
        return [
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_top, 30, 25), 0),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_top, 30, 20), 0.5),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_top, 30, 15), 0.5),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_top, 30, 10), 0.5),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_top, 30, 5), 0.5),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_top, 30, 0), 0.5),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_top, 30, -5), 0.5),
        ]

    def triangles_from_bottom(self):
        return [
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_bottom, 30, -25), 0),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_bottom, 30, -20), 0.5),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_bottom, 30, -15), 0.5),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_bottom, 30, -10), 0.5),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_bottom, 30, -5), 0.5),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_bottom, 30, 0), 0.5),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_from_bottom, 30, 5), 0.5),
        ]

    def triangles_in_triangle_formation(self):
        return [
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_straight, 30, 0), 0),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_straight, 30, 5), 0.5),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_straight, 30, -5), 0),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_straight, 30, 10), 0.5),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_straight, 30, -10), 0),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_straight, 30, 15), 0.5),
            EnemyScheduling(lambda: self.__add_enemy(enemy_triangle_straight, 30, -15), 0),
        ]

    def two_octogons_in_parallel(self):
        return [
            EnemyScheduling(lambda: self.__add_enemy(enemy_octogon, 30, 10), 0),
            EnemyScheduling(lambda: self.__add_enemy(enemy_octogon, 30, -10), 0),
        ]


def enemy_triangle_straight():
    return EnemyFactory.create_enemy(
        EnemyBodyHitboxComponentTupleCollection.basic_triangle(),
        EnemyMoveComponentCollection.from_center_go_straight(),
        EnemyShootPatternComponentCollection.basic_bullet(bullets_per_second=10, direction_variability=30, burst_duration_seconds=0.3, pause_duration_seconds=1.5),
        hit_points=1
    )


def enemy_triangle_from_top():
    return EnemyFactory.create_enemy(
        EnemyBodyHitboxComponentTupleCollection.basic_triangle(),
        EnemyMoveComponentCollection.from_top_go_down_up_straight(),
        EnemyShootPatternComponentCollection.basic_bullet(bullets_per_second=8, direction_variability=0, burst_duration_seconds=0.3, pause_duration_seconds=1.5),
        hit_points=1
    )


def enemy_triangle_from_bottom():
    return EnemyFactory.create_enemy(
        EnemyBodyHitboxComponentTupleCollection.basic_triangle(),
        EnemyMoveComponentCollection.from_bottom_go_up_down_straight(),
        EnemyShootPatternComponentCollection.basic_bullet(bullets_per_second=8, direction_variability=0, burst_duration_seconds=0.3, pause_duration_seconds=1.5),
        hit_points=1
    )


def enemy_triangle_big():
    return EnemyFactory.create_enemy(
        EnemyBodyHitboxComponentTupleCollection.big_triangle(),
        EnemyMoveComponentCollection.from_center_static_go_down_up_down_twice_then_ram(),
        EnemyShootPatternComponentCollection.two_long_basic_bullet_bursts_big_bullet_scatter(),
        hit_points=20
    )


def enemy_octogon():
    return EnemyFactory.create_enemy(
        EnemyBodyHitboxComponentTupleCollection.octogon(),
        EnemyMoveComponentCollection.from_center_go_straight_slow(),
        EnemyShootPatternComponentCollection.explosion_like_bullet(),
        hit_points=5
    )
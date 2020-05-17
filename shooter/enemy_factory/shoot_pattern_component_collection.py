from game_engine.component import ParticleEmitterComponent
from game_engine.component.shoot_pattern_component import ShootPatternComponentNode, ShootPatternComponent
from game_engine.geometry import Vector3D

from shooter.enemy_factory.enemy_bullets import BasicBullet, BigBullet


class EnemyShootPatternComponentCollection(object):
    @classmethod
    def basic_bullet(cls, bullets_per_second, direction_variability, burst_duration_seconds, pause_duration_seconds):
        particle_emitter = ParticleEmitterComponent(
            BasicBullet,
            bullets_per_second,
            Vector3D(-15, 0, 0),
            speed_variability=0,
            direction_variability=direction_variability
        )
        shoot_pattern_node_list = [
                                      ShootPatternComponentNode(particle_emitter, burst_duration_seconds),
                                      ShootPatternComponentNode(None, pause_duration_seconds),
                                  ] * 999
        return ShootPatternComponent(shoot_pattern_node_list)

    @classmethod
    def explosion_like_bullet(cls):
        return cls.basic_bullet(100, 180, 0.1, 1)

    @classmethod
    def two_long_basic_bullet_bursts_big_bullet_scatter(cls):
        particle_emitter_straight = ParticleEmitterComponent(
            BasicBullet,
            10,
            Vector3D(-15, 0, 0),
            speed_variability=0,
            direction_variability=0
        )
        particle_emitter_scatter = ParticleEmitterComponent(
            BigBullet,
            40,
            Vector3D(-20, 0, 0),
            speed_variability=0,
            direction_variability=60
        )
        shoot_pattern_node_list = [
                                      ShootPatternComponentNode(None, 3),
                                  ] + [
                                      ShootPatternComponentNode(particle_emitter_straight, 2),
                                      ShootPatternComponentNode(None, 1),
                                      ShootPatternComponentNode(particle_emitter_straight, 2),
                                      ShootPatternComponentNode(None, 3),
                                      ShootPatternComponentNode(particle_emitter_scatter, 2),
                                  ] + [
                                      ShootPatternComponentNode(particle_emitter_straight, 2),
                                      ShootPatternComponentNode(None, 1),
                                      ShootPatternComponentNode(particle_emitter_straight, 2),
                                      ShootPatternComponentNode(None, 3),
                                      ShootPatternComponentNode(particle_emitter_scatter, 2),
                                  ] * 60
        return ShootPatternComponent(shoot_pattern_node_list)

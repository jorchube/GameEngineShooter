from shooter.enemies.enemy import Enemy


class EnemyFactory(object):
    @classmethod
    def create_enemy(cls, body_hitbox_component_tuple, move_component, shoot_pattern_component, hit_points):
        e = Enemy(hit_points=hit_points)
        e.add_component(body_hitbox_component_tuple[0])
        e.add_component(body_hitbox_component_tuple[1])
        e.add_component(shoot_pattern_component)
        e.add_component(move_component)
        return e

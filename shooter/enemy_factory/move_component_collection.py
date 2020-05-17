from game_engine.component.move_component import MoveComponentNode, MoveComponent
from game_engine.geometry import Vector3D


class EnemyMoveComponentCollection(object):
    @classmethod
    def from_center_go_straight(cls):
        return MoveComponent([
            MoveComponentNode(Vector3D(-5, 0, 0), 999)
        ])

    @classmethod
    def from_top_go_down_up_straight(cls):
        return MoveComponent([
            MoveComponentNode(Vector3D(-4, -6, 0), 3),
            MoveComponentNode(Vector3D(-4, 6, 0), 1.5),
            MoveComponentNode(Vector3D(-5, 0, 0), 999)
        ])

    @classmethod
    def from_bottom_go_up_down_straight(cls):
        return MoveComponent([
            MoveComponentNode(Vector3D(-4, 6, 0), 3),
            MoveComponentNode(Vector3D(-4, -6, 0), 1.5),
            MoveComponentNode(Vector3D(-5, 0, 0), 999)
        ])

    @classmethod
    def from_center_go_straight_slow(cls):
        return MoveComponent([
            MoveComponentNode(Vector3D(-3, 0, 0), 999)
        ])

    @classmethod
    def from_center_static_go_down_up_down_twice_then_ram(cls):
        return MoveComponent([
            MoveComponentNode(Vector3D(-5, 0, 0), 3),
        ] + [
            MoveComponentNode(Vector3D(0, -8, 0), 2),
            MoveComponentNode(Vector3D(0, 8, 0), 4),
            MoveComponentNode(Vector3D(0, -8, 0), 2),
            MoveComponentNode(Vector3D(0, 0, 0), 2)
        ] + [
            MoveComponentNode(Vector3D(0, -8, 0), 2),
            MoveComponentNode(Vector3D(0, 8, 0), 4),
            MoveComponentNode(Vector3D(0, -8, 0), 2),
        ] + [
            MoveComponentNode(Vector3D(-12, 0, 0), 999)
        ])


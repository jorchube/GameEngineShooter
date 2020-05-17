from game_engine.component import PolygonComponent, HitboxComponent
from game_engine.geometry import Point3D, Polygon
from game_engine.geometry.primitive_shapes import PrimitiveShapes


class EnemyBodyHitboxComponentTupleCollection(object):
    @classmethod
    def basic_triangle(cls):
        body = Polygon([Point3D(-1, 0, 0), Point3D(1, -1, 0), Point3D(1, 1, 0)])
        return PolygonComponent(body), HitboxComponent(body, is_collision_source=True)

    @classmethod
    def big_triangle(cls):
        body = Polygon([Point3D(-3, 0, 0), Point3D(3, -3, 0), Point3D(3, 3, 0)])
        return PolygonComponent(body), HitboxComponent(body, is_collision_source=True)

    @classmethod
    def octogon(cls):
        body = PrimitiveShapes.octogon(2, 30)
        return PolygonComponent(body), HitboxComponent(body, is_collision_source=True)
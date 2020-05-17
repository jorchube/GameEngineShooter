from game_engine.actor import Particle
from game_engine.event.event_dispatcher import EventDispatcher
from game_engine.event.event_type import collision_event
from game_engine.event.event_type.add_actor_to_scene_event import AddActorToSceneEvent
from game_engine.event.event_type.remove_actor_from_scene_event import RemoveActorFromSceneEvent
from game_engine.geometry.primitive_shapes import PrimitiveShapes
from game_engine.geometry.vector import Vector3D
from game_engine.component.polygon_component import PolygonComponent
from game_engine.component.hitbox_component import HitboxComponent
from game_engine.component.color_component import ColorComponent
from game_engine.visual import RGB

from shooter.effects.bullet_hit import BulletHit


class Bullet(Particle):
    def __init__(self, lifespan=10, hit_damage=1):
        super().__init__(lifespan)
        body = PrimitiveShapes.rectangle(0.2, 0.2, 45)
        body.translate(Vector3D(-0.05, -0.05, 0))
        self.add_component(PolygonComponent(body))
        self.add_component(HitboxComponent(body))
        self.add_component(ColorComponent(RGB(1, 0.4, 0.4)))
        self.__subscribe_to_events()
        self.__hit_damage = hit_damage

    @property
    def hit_damage(self):
        return self.__hit_damage

    def __subscribe_to_events(self):
        self.subscribe_to_event(collision_event.CollisionEvent, self.__on_collision_event)

    def __on_collision_event(self, event):
        hit = BulletHit()
        hit.position = self.position
        EventDispatcher.append_event(AddActorToSceneEvent(hit))
        EventDispatcher.append_event(RemoveActorFromSceneEvent(self))


class BigBullet(Bullet):
    def __init__(self, lifespan=10, hit_damage=1):
        super().__init__(lifespan, hit_damage)
        body = PrimitiveShapes.rectangle(0.3, 0.3, 45)
        body.translate(Vector3D(-0.05, -0.05, 0))
        self.delete_all_components()
        self.add_component(PolygonComponent(body))
        self.add_component(HitboxComponent(body))
        self.add_component(ColorComponent(RGB(1, 0.4, 0.4)))

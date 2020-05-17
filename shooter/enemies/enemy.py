from game_engine.actor import Actor
from game_engine.event.event_dispatcher import EventDispatcher
from game_engine.event.event_type import collision_event
from game_engine.event.event_type.add_actor_to_scene_event import AddActorToSceneEvent
from game_engine.event.event_type.remove_actor_from_scene_event import RemoveActorFromSceneEvent

from shooter import collision_masks
from shooter.effects.explosion import Explosion


class Enemy(Actor):
    def __init__(self, hit_points=1):
        super().__init__()
        self.collision_mask = collision_masks.PLAYER_BULLET
        self.__subscribe_to_events()
        self.__hp = hit_points
        self.__scene_removal_threshold = 35

    @property
    def hit_points(self):
        return self.__hp

    @hit_points.setter
    def hit_points(self, value):
        self.__hp = value

    def __subscribe_to_events(self):
        self.subscribe_to_event(collision_event.CollisionEvent, self.__on_collision_event)

    def __on_collision_event(self, event):
        try:
            self.__hp -= event.colliding_actor.hit_damage
        except AttributeError:
            pass

        if self.__hp <= 0:
            self.__destroyed()

    def __destroyed(self):
        explosion = Explosion()
        explosion.position = self.position
        EventDispatcher.append_event(AddActorToSceneEvent(explosion))
        EventDispatcher.append_event(RemoveActorFromSceneEvent(self))

    def end_tick(self):
        super().end_tick()
        if self.__is_out_of_scene():
            EventDispatcher.append_event(RemoveActorFromSceneEvent(self))

    def __is_out_of_scene(self):
        return abs(self.position.x) > self.__scene_removal_threshold or abs(self.position.y) > self.__scene_removal_threshold

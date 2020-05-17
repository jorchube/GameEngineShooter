import random

from game_engine.actor import Particle
from game_engine.component import PolygonComponent, ColorComponent, OutlineComponent
from game_engine.event import CollisionEvent
from game_engine.geometry.primitive_shapes import PrimitiveShapes
from game_engine.visual import RGB

from shooter.effects.sound import SoundEffects


class BulletHit(Particle):
    lifespan_seconds = 0.1

    def __init__(self):
        super().__init__(lifespan_seconds=BulletHit.lifespan_seconds)
        body = PrimitiveShapes.star4arms(0.3, 0.1, rotation=random.randint(0, 89))
        self.add_component(PolygonComponent(body))
        self.add_component(ColorComponent(RGB(1, 0.5, 0)))
        self.add_component(OutlineComponent(RGB(0.5, 1, 0), thickness=1))
        self.sound_played = False

    def end_tick(self):
        super().end_tick()
        if not self.sound_played:
            SoundEffects.bullet_impact()
            self.sound_played = True



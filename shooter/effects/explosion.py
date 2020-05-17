import random

from game_engine.actor import Particle
from game_engine.component import PolygonComponent, ColorComponent, OutlineComponent, ParticleEmitterComponent
from game_engine.geometry import Vector3D
from game_engine.geometry.primitive_shapes import PrimitiveShapes
from game_engine.visual import RGB

from shooter.effects.sound import SoundEffects


class ExplosionParticle(Particle):
    def __init__(self):
        lifespan = random.uniform(0.5, 2)
        super().__init__(lifespan)
        self.add_component(PolygonComponent(PrimitiveShapes.triangle(0.2)))
        self.add_component(ColorComponent(RGB.random()))


class Explosion(Particle):
    lifespan_seconds = 0.1

    def __init__(self):
        super().__init__(Explosion.lifespan_seconds)

        body = PrimitiveShapes.star4arms(3, 0.5, rotation=random.randrange(0, 89))
        body_component = PolygonComponent(body)
        body_component.add_component(ColorComponent(RGB.random()))
        body_component.add_component(OutlineComponent(RGB.random(), thickness=1))
        self.add_component(body_component)

        body = PrimitiveShapes.octogon(2, rotation=random.randint(0, 89))
        body_component = PolygonComponent(body)
        body_component.add_component(ColorComponent(RGB.random()))
        body_component.add_component(OutlineComponent(RGB.random(), thickness=1))
        self.add_component(body_component)

        self.add_component(ParticleEmitterComponent(
            ExplosionParticle,
            100,
            Vector3D(5, 0, 0),
            speed_variability=0.5,
            direction_variability=360
        ))

        self.sound_played = False

    def end_tick(self):
        super().end_tick()
        if not self.sound_played:
            SoundEffects.explosion()
            self.sound_played = True

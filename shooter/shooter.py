from game_engine.display.display_configuration import DisplayConfiguration
from game_engine.game import Game
from game_engine.geometry import Point3D, Rotation
from game_engine.visual import Camera

from shooter.effects.sound import SoundEffects
from shooter.player.player import Player
from shooter.scenes.scene1 import Scene1


def start():
    display_configuration = DisplayConfiguration(width_px=800, height_px=600, fps=60, scaled=True)
    camera = Camera(Point3D(0, 0, -50), Rotation(0, 0, 0), 45, 0.1, 100)

    Game.initialize(display_configuration, camera, Scene1)

    SoundEffects.initialize()

    Game.current_scene().add_actor(Player())
    Game.run()


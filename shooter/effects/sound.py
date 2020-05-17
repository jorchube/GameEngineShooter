from game_engine.audio import Audio


class SoundEffects(object):
    __bullet_impact = None
    __explosion = None

    @classmethod
    def initialize(cls):
        cls.__bullet_impact = Audio.new_sound('resources/audio/click.wav')
        cls.__explosion = Audio.new_sound('resources/audio/explosion.wav')

    @classmethod
    def explosion(cls):
        cls.__explosion.play()

    @classmethod
    def bullet_impact(cls):
        cls.__bullet_impact.play()
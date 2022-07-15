from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideShipAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        #ball = cast.get_first_actor(BALL_GROUP)
        ship = cast.get_first_actor(SHIP_GROUP)
        
        #ball_body = ball.get_body()
        ship_body = ship.get_body()

        #if self._physics_service.has_collided(ball_body, racket_body):
         #   sound = Sound(BOUNCE_SOUND)
        #  self._audio_service.play_sound(sound)    
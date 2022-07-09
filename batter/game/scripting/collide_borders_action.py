from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.ball import Ball
from game.casting.body import Body
from game.casting.image import Image
from game.casting.point import Point


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
                
        if y < FIELD_TOP:
            cast.remove_actor(BALL_GROUP, ball)
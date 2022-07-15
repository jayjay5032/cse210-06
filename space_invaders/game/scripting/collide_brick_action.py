from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.ball import Ball
from game.casting.body import Body
from game.casting.image import Image
from game.casting.point import Point




class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        bricks = cast.get_actors(BRICK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for brick in bricks:
            balls = cast.get_actors(BALL_GROUP)
            if len(balls) != 0: 
                ball = cast.get_first_actor(BALL_GROUP)
                ball_body = ball.get_body()
                brick_body = brick.get_body()

                if self._physics_service.has_collided(ball_body, brick_body):
                    sound = Sound(BOUNCE_SOUND)
                    self._audio_service.play_sound(sound)
                    points = brick.get_points()
                    stats.add_points(points)
                    cast.remove_actor(BRICK_GROUP, brick)
                    cast.remove_actor(BALL_GROUP, ball)

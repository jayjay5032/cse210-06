from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.ball import Ball
from game.casting.body import Body
from game.casting.brick import Brick
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.racket import Racket


class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        bricks = cast.get_actors(BRICK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for brick in bricks:
            ball_body = ball.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(ball_body, brick_body):
                #ball.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                cast.remove_actor(BRICK_GROUP, brick)
                cast.remove_actor(BALL_GROUP, ball)
                cast.clear_actors(BALL_GROUP)
                x = CENTER_X - BALL_WIDTH / 2
                y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
                position = Point(x, y)
                size = Point(BALL_WIDTH, BALL_HEIGHT)
                velocity = Point(0, 0)
                body = Body(position, size, velocity)
                image = Image(BALL_IMAGE)
                ball = Ball(body, image, True)
                cast.add_actor(BALL_GROUP, ball)
from constants import *
from game.scripting.action import Action
from game.casting.ball import Ball
from game.casting.body import Body
from game.casting.image import Image
from game.casting.point import Point

class ReloadBallAction(Action):
    
    def execute(self, cast, script, callback):  
        x = cast.get_first_actor(RACKET_GROUP).get_body().get_position().get_x() + (RACKET_WIDTH/2) - (BALL_WIDTH/2)
        y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP, ball)
        ball.release()

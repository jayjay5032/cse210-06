from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        racketbody = racket.get_body()
        racketvelocity = racketbody.get_velocity()
        racketposition = racketbody.get_position()
        racketx = racketposition.get_x()
        racketposition = racketposition.add(racketvelocity)
        
        ball = cast.get_first_actor(BALL_GROUP)
        ballbody = ball.get_body()
        ballvelocity = racketvelocity
        ballposition = ballbody.get_position()
        ballposition = ballposition.add(ballvelocity)

        if racketx < 0:
            racketposition = Point(0, racketposition.get_y())
            ballposition = Point(RACKET_WIDTH/2 - BALL_WIDTH/2, ballposition.get_y())
        elif racketx > (SCREEN_WIDTH - RACKET_WIDTH):
            racketposition = Point(SCREEN_WIDTH - RACKET_WIDTH, racketposition.get_y())
            ballposition = Point(SCREEN_WIDTH - RACKET_WIDTH/2 - BALL_WIDTH/2, ballposition.get_y())
            
        racketbody.set_position(racketposition)
        ballbody.set_position(ballposition)
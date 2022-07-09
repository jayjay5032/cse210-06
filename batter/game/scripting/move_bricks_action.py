from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveBricksAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        bricks = cast.get_actors(BRICK_GROUP)

        for i in bricks:

            body = i.get_body()
            velocity = body.get_velocity()
            position = body.get_position()
            x = position.get_x()
        
            position = position.add(velocity)

            if x < 0 - (BRICK_WIDTH * .25):
                velocity = Point(BRICK_VELOCITY, 0)
            elif x > (SCREEN_WIDTH - (BRICK_WIDTH * .75)):
                velocity = Point(-BRICK_VELOCITY, 0)
                
            body.set_position(position)

            for i in bricks:
                
                body = i.get_body()
                body.set_velocity(velocity)
        
        
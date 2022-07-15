from importlib import reload
from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveBricksAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        bricks = cast.get_actors(BRICK_GROUP)
        if len(bricks) != 0:         
            firstbrick= cast.get_first_actor(BRICK_GROUP)
            first_x = firstbrick.get_body().get_position().get_x()
            lastbrick = cast.get_last_actor(BRICK_GROUP)
            last_x = lastbrick.get_body().get_position().get_x()

            
            for i in bricks:
                if first_x <= 0:
                        i.swing_right()
                elif last_x + BRICK_WIDTH >= SCREEN_WIDTH:
                        i.swing_left()
                i.move_next()
            
        
from importlib import reload
from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveEnemiesAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        enemys = cast.get_actors(ENEMY_GROUP)
        if len(enemys) != 0:         
            firstenemy= cast.get_first_actor(ENEMY_GROUP)
            first_x = firstenemy.get_body().get_position().get_x()
            lastenemy = cast.get_last_actor(ENEMY_GROUP)
            last_x = lastenemy.get_body().get_position().get_x()

            
            for i in enemys:
                if first_x <= 0:
                        i.swing_right()
                elif last_x + ENEMY_WIDTH >= SCREEN_WIDTH:
                        i.swing_left()
                i.move_next()
            
        
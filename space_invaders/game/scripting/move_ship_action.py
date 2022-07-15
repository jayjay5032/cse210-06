from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveShipAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP)
        shipbody = ship.get_body()
        shipvelocity = shipbody.get_velocity()
        shipposition = shipbody.get_position()
        shipx = shipposition.get_x()
        shipposition = shipposition.add(shipvelocity)
        if shipx < 0:
            shipposition = Point(0, shipposition.get_y())
        elif shipx > (SCREEN_WIDTH - SHIP_WIDTH):
            shipposition = Point(SCREEN_WIDTH - SHIP_WIDTH, shipposition.get_y())
        shipbody.set_position(shipposition)
        
        # If bullet is on the ship then follow it, otherwise don't follow
        bullets = cast.get_actors(BULLET_GROUP)
        if len(bullets) != 0:
            bullet = cast.get_first_actor(BULLET_GROUP)
            bulletbody = bullet.get_body()
            bulletposition = bulletbody.get_position()
            if bulletposition.get_y() == SCREEN_HEIGHT - BULLET_HEIGHT - SHIP_HEIGHT:
                bulletvelocity = shipvelocity
                bulletposition = bulletposition.add(bulletvelocity)
                if shipx < 0:
                    bulletposition = Point(SHIP_WIDTH/2 - BULLET_WIDTH/2, bulletposition.get_y())
                elif shipx > (SCREEN_WIDTH - SHIP_WIDTH):
                    bulletposition = Point(SCREEN_WIDTH - SHIP_WIDTH/2 - BULLET_WIDTH/2, bulletposition.get_y())
                bulletbody.set_position(bulletposition)
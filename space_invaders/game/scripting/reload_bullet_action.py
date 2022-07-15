from constants import *
from game.scripting.action import Action
from game.casting.bullet import Bullet
from game.casting.body import Body
from game.casting.image import Image
from game.casting.point import Point

class ReloadBulletAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
    
    def execute(self, cast, script, callback):
        bullets = cast.get_actors(BULLET_GROUP)  
        if len(bullets) == 0:
            x = cast.get_first_actor(SHIP_GROUP).get_body().get_position().get_x() + (SHIP_WIDTH/2) - (BULLET_WIDTH/2)
            y = SCREEN_HEIGHT - SHIP_HEIGHT - BULLET_HEIGHT  
            position = Point(x, y)
            size = Point(BULLET_WIDTH, BULLET_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(BULLET_IMAGE)
            bullet = Bullet(body, image, True)
            cast.add_actor(BULLET_GROUP, bullet)

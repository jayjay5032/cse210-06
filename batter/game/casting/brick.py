import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Brick(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, animation, points, debug = False):
        """Constructs a new Brick.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._points = points
        
    def get_animation(self):
        """Gets the brick's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the brick's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the brick's points.
        
        Returns:
            A number representing the brick's points.
        """
        return self._points

    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)
    
    def stop_moving(self):
        """Stops the bat from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)
        
    def release(self):
        """Release the ball in a random direction."""
        rn = random.uniform(0.9, 1.1)
        vx = random.choice([-BRICK_VELOCITY * rn, BRICK_VELOCITY * rn])
        vy = -BRICK_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)
import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Enemy(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, animation, points, debug = False):
        """Constructs a new Enemy.
        
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
        """Gets the enemy's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the enemy's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the enemy's points.
        
        Returns:
            A number representing the enemy's points.
        """
        return self._points

    def move_next(self):
        """Moves the enemys using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """Steers the enemys to the left."""
        velocity = Point(-ENEMY_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def swing_right(self):
        """Steers the enemys to the right."""
        velocity = Point(ENEMY_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the enemys from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)
        
    def release(self):
        """Release the enemys in a random direction."""
        velocity = Point(ENEMY_VELOCITY, 0)
        self._body.set_velocity(velocity)
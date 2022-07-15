from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action

class CollideEnemyAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        enemys = cast.get_actors(ENEMY_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for enemy in enemys:
            bullets = cast.get_actors(BULLET_GROUP)
            if len(bullets) != 0: 
                bullet = cast.get_first_actor(BULLET_GROUP)
                bullet_body = bullet.get_body()
                enemy_body = enemy.get_body()

                if self._physics_service.has_collided(bullet_body, enemy_body):
                    sound = Sound(BOUNCE_SOUND)
                    self._audio_service.play_sound(sound)
                    points = enemy.get_points()
                    stats.add_points(points)
                    cast.remove_actor(ENEMY_GROUP, enemy)
                    cast.remove_actor(BULLET_GROUP, bullet)

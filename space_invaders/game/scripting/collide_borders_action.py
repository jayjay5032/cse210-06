from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action

class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        bullet = cast.get_first_actor(BULLET_GROUP)
        body = bullet.get_body()
        position = body.get_position()
        y = position.get_y()

                
        if y < FIELD_TOP - ((BULLET_HEIGHT + HUD_MARGIN)*3):
            cast.remove_actor(BULLET_GROUP, bullet)
            explode_sound = Sound(EXPLODE_SOUND)
            self._audio_service.play_sound(explode_sound)
            stats = cast.get_first_actor(STATS_GROUP)
            stats.lose_life()
            
            if stats.get_lives() > 0:
                callback.on_next(TRY_AGAIN) 
            else:
                callback.on_next(GAME_OVER)
                over_sound = Sound(OVER_SOUND)
                self._audio_service.play_sound(over_sound)
from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action

class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
                
        if y < FIELD_TOP - ((BALL_HEIGHT + HUD_MARGIN)*3):
            cast.remove_actor(BALL_GROUP, ball)
            self._audio_service.play_sound(bounce_sound)
            stats = cast.get_first_actor(STATS_GROUP)
            stats.lose_life()
            
            if stats.get_lives() > 0:
                callback.on_next(TRY_AGAIN) 
            else:
                callback.on_next(GAME_OVER)
                over_sound = Sound(OVER_SOUND)
                self._audio_service.play_sound(over_sound)
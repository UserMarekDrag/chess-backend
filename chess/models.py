from django.db import models

class Game(models.Model):
    board_state = models.JSONField(default=dict)
    game_status = models.CharField(max_length=11, choices=[('IN_PROGRESS', 'In Progress'), ('FINISHED', 'Finished')], default='IN_PROGRESS')
    current_turn = models.CharField(max_length=5, choices=[('WHITE', 'White'), ('BLACK', 'Black')], default='WHITE', db_index=True)
    move_log = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"Game {self.pk}: {self.game_status}"

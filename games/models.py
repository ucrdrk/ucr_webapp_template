from django.db import models

class Games(models.Model):
    game_name = models.CharField(max_length=100)
    game_file = models.CharField(max_length=100)
    file_location = models.CharField(max_length=100)
    game_year = models.IntegerField()
    cover = models.FileField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.game_name
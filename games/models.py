from django.db import models

class Games(models.Model):
    game_name = models.CharField(max_length=100)
    game_file_link = models.CharField(max_length=100)
    file_location = models.CharField(max_length=100)
    game_year = models.IntegerField()
    cover = models.FileField(upload_to='covers/', blank=True)
    rma_file = models.FileField(upload_to='rmaFolder/', blank=True)
    stored_TF = models.BooleanField(default=False) #For the script on the mister to see if its downloaded or not.
                                                   #Default value no game is stored.

    remove_TF = models.BooleanField(default=False) # For the front end to signify that it has been removed.
                                                #could use this for the ADDED/REMOVE button signal.
                                                #on first click the game is added value is 0. Once Removed is clicked....
                                                #the value is 1 so the script knows to delete it.
    def __str__(self):
        return self.game_name
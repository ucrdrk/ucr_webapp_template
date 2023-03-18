from django.db import models
from django.contrib.auth.models import AbstractUser
from games.models import Games #Get the data model from games

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid

# Create your models here.
class User(AbstractUser):
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to ='avatars/', null=True, blank=True)
    game = models.ManyToManyField('games.Games', blank=True)

    play_flag = models.CharField(max_length=1000)
    sync_flag = models.BooleanField(default = False)
    sync_done_flag = models.BooleanField(default = False)
    updated= models.DateTimeField(blank=True) #auto_now is updated whenever a value is updated
    current_storage = models.FloatField(blank=True)
    total_storage = models.FloatField(blank=True)

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
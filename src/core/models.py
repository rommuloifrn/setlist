from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Create your models here.

class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

class GroupAssociation(models.Model):
    class Role(models.TextChoices):
        MANAGER = "MAN", _("Manager")
        MEMBER = "MEM", _("Member")

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=3, choices=Role.choices, default=Role.MEMBER)


class Music(models.Model):
    class Tone(models.TextChoices):
        MINOR_DO = "Cm", "Dó menor"
        # add missing ones

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    # tone
    # lenght

class Setlist(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    musics = models.ManyToManyField(Music)

class Tag(models.Model):
    musics = models.ManyToManyField(Music)
    title = models.CharField(max_length=30)

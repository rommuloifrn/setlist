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

class AssociationRequest(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    destinatary = models.ForeignKey(User, on_delete=models.CASCADE)

class Music(models.Model):
    class Tone(models.TextChoices):
        DO = "C", "Dó maior"
        MINOR_DO = "Cm", "Dó menor"
        DO_SUS = "C#", "Dó sustenido"
        DO_SUS_MINOR = "C#m", "Dó sustenido menor"
        
        RE = "D", "Ré"
        RE_MINOR = "Dm", "Ré menor"
        RE_SUS = "D#", "Ré sustenido"
        RE_SUS_MINOR = "D#m", "Ré sustenido menor"
        
        MI = "E", "Mi"
        MI_MINOR = "Em", "Mi menor"
        
        FA = "F", "Fá"
        FA_MINOR = "Fm", "Fá menor"
        FA_SUS = "F#", "Fá sustenido"
        FA_SUS_MINOR = "F#m", "Fá sustenido menor"
        
        SOL = "G", "Sol"
        SOL_MINOR = "Gm", "Sol menor"
        SOL_SUS = "G#", "Sol sustenido"
        SOL_SUS_MINOR = "G#m", "Sol sustenido menor"
        
        LA = "A", "Lá"
        LA_MINOR = "Am", "Lá menor"
        LA_SUS = "A#", "Lá sustenido"
        LA_SUS_MINOR = "A#m", "Lá sustenido menor"
        
        SI = "B", "Si"
        SI_MINOR = "Bm", "Si menor"

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    tone = models.CharField(max_length=4, choices=Tone.choices, default=Tone.MI)
    lenght = models.DurationField()

class Setlist(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    musics = models.ManyToManyField(Music)

class Tag(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    musics = models.ManyToManyField(Music)
    title = models.CharField(max_length=30)

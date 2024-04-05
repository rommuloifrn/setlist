from django.contrib import admin
from .models import Group, GroupAssociation, Music, Setlist, Tag

# Register your models here.

admin.site.register(Group)
admin.site.register(GroupAssociation)
admin.site.register(Music)
admin.site.register(Setlist)
admin.site.register(Tag)
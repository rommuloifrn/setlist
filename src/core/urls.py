from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("groups", views.groups, name="groups"),
    path("group/<int:id>", views.read_group, name="r_group")
]

from django.shortcuts import render
from .models import Group

# Create your views here.
def index(request):
    return render(request, "index.html")

def groups(request):
    groups = Group.objects.all()
    return render(request, "groups.html", {"groups":groups})
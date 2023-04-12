from django.shortcuts import render

from lelang.models import User


def index(request):
    users = User.objects.all()
    return render(request, "index.html", context={"users": users})

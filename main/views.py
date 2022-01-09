from django.shortcuts import render, redirect
from .models import Destination, USER_subs
# import datetime
from datetime import datetime
import pymongo
from .Connect import collection_sub,collection_dest
# Create your views here.


def index(request):
    dests = Destination.objects.all()
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    return render(request, "index.html", {
        'destinations': dests
    })


def sub(request):

    name = request.POST['name']
    email = request.POST['email']

    if USER_subs.objects.filter(email=email).exists():
        print("already exists")
        return redirect('/')
    else:
        user_sub = USER_subs(name=name, email=email)
        user_sub.save()
        print("added")
        return redirect('/')



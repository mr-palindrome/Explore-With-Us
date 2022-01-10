from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import Destination, USER_subs
import pymongo
from .Connect import collection


# Create your views here.


def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {
        'destinations': dests,
    })


def sub(request):
    name = request.POST['name']
    email = request.POST['email']

    if USER_subs.objects.filter(email=email).exists():
        return redirect('/')
    else:
        user_sub = USER_subs(name=name, email=email)
        user_sub.save()
        return redirect('/')


# /search/?address=
def search(request):
    address = ''
    address = request.GET.get('address')
    payload = []
    if address:
        add_result = collection.aggregate(
            [
                {
                    "$search": {
                        "autocomplete": {
                            "query": address,
                            "path": "name",
                            "fuzzy": {
                                "maxEdits": 2
                            }
                        }
                    }
                }
            ]
        )
        for i in add_result:
            payload.append(i['name'])
    return JsonResponse({'data': payload
    })


def result(request, destname):
    payload = []
    if destname:
        add_result = collection.aggregate(
            [
                {
                    "$search": {
                        "autocomplete": {
                            "query": destname,
                            "path": "name",
                        }
                    }
                },
                {
                    '$project': {
                        "id": 1,
                    }
                }
            ]
        )
        for i in add_result:
            payload.append(i['id'])
        dests = Destination.objects.filter(id__in=payload)
        if not payload:
            return redirect('/')
    else:
        return redirect('/')
    return render(request, "index.html", {
        'destinations': dests,
    })

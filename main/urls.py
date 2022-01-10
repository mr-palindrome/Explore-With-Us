from django.urls import path

from . import views

urlpatterns = [
    # Path converters
    # int: numbers
    # str: strings
    # path: whole urls /
    # slug: hyphen-and_underscore_stuff
    # UUID: universally unique identifier like username
    path('', views.index),
    path('subscribe', views.sub, name='sub'),
    path('search/', views.search),
    path('dests/<str:destname>', views.result),

]


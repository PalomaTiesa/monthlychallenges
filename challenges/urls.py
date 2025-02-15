from django.urls import path
from . import views

urlpatterns = [
path("index/", views.index),
path("january/", views.january),
path("february/", views.february),
path("march/", views.march),
path("april/", views.april),
path("may/", views.may),
path("june/", views.june),
path("july/", views.july),
path("august/", views.august),
path("september/", views.september),
path("october/", views.october),
path("november/", views.november),
path("december/", views.december),
]

#http://127.0.0.1:8000/challenges

#http://127.0.0.1:8000/january

#http://127.0.0.1:8000/february

#http://127.0.0.1:8000/march

#http://127.0.0.1:8000/april

#http://127.0.0.1:8000/may

#http://127.0.0.1:8000/june

#http://127.0.0.1:8000/july

#http://127.0.0.1:8000/august

#http://127.0.0.1:8000/september

#http://127.0.0.1:8000/november

#http://127.0.0.1:8000/december
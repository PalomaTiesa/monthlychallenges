from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Este es un mensaje para el index.")

def january(request):
    return HttpResponse("Walk for at least 30 min every day.")

def february(request):
    return HttpResponse("Go to the gym every day.")

def march(request):
    return HttpResponse("Eat healthy.")

def april(request):
    return HttpResponse("Run in the morning.")

def may(request):
    return HttpResponse("Go to church.")

def june(request):
    return HttpResponse("Go on a trip.")

def july(request):
    return HttpResponse("Learn a new sport.")

def august(request):
    return HttpResponse("Read a new book.")

def september(request):
    return HttpResponse("Learn to dance.")

def october(request):
    return HttpResponse("Buy new computer.")

def november(request):
    return HttpResponse("Go skiing")

def december(request):
    return HttpResponse("Prepare the christmas decorations.")
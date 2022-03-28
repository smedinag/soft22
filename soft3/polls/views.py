from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hola mundo!. Estás en el index de polls!.")

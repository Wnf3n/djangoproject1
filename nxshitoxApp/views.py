from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return HttpResponse("Hellooooo")

def inicio(request):
    return render(request,'paginas/inicio.html')

def ver(request):
    return render(request,'paginas/ver.html')
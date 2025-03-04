from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("List of cars")
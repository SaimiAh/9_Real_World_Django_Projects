from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello")

def item(request):
    return HttpResponse("This is the item.")



from django.shortcuts import render
from django.http import HttpResponse

def function_2(request):
    return HttpResponse("Hello Django app two")


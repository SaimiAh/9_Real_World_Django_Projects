from django.http import HttpResponse
from django.shortcuts import render
from food.models import Item
from django.template import loader

def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context  = {
        
    }
    return HttpResponse(template.render(context, request))

def item(request):
    return HttpResponse("This is the item.")



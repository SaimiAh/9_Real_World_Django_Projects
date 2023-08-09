from django.http import HttpResponse
from django.shortcuts import render,redirect
from food.models import Item
from django.template import loader
from .forms import ItemForm


#HOME VIEW
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context  = {
        'item_list':item_list,
    }
    return render(request, 'food/index.html', context)


#NULL VIEW
def item(request):
    return HttpResponse("This is the item.")


#CREATE VIEW
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form':form})


#READ VIEW
def details(request,item_id):
    item_details=Item.objects.get(pk=item_id)
    context  = {
        'item_details':item_details,
    }
    return render(request, 'food/details.html', context)


# UPADTE VIEW
def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form':form, 'item':item,})


# DELETE VIEW 
def delete_item(request,id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item':item})

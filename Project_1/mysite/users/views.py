from django.shortcuts import render,redirect
from .forms import RegisterationForm
from django.contrib import messages

#ResgisterationForm View
def register(request):
    if request.method=="POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome you are sucessfully registered {username}.')
            return redirect('food:index')
    else:   
        form = RegisterationForm()
    return render(request, 'users/register.html', {'form':form,})

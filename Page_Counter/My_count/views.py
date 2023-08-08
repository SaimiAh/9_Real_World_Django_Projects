from django.shortcuts import render

def home(request):
    ct = request.session.get('count', 0)
    new_count = ct+1
    request.session['count'] = new_count
    return render(request, 'My_count/home.html', {'c': new_count})

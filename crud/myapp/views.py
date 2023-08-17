from django.shortcuts import render, redirect
from myapp.models import Student

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rollnumber = request.POST.get('rollnumber')
        student=Student.object.create(name=name,rollnumber=rollnumber)
        return redirect('home')
    students = Student.objects.all()
    return render(request, 'myapp/home.html', {'students': students})


def update(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        rollnumber = request.POST.get('rollnumber')
        student.name = name
        student.rollnumber = rollnumber
        student.save()
        return redirect('home')
    return render(request, 'myapp/update.html', {'student': student})

def delete(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request, 'myapp/delete.html', {'student': student})

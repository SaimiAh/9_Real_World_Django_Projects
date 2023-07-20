from django.shortcuts import render

# Create your views here.
from enroll.models import Student
 
def stuinfo(request):
    stud=Student.objects.all()
    return render(request, 'enroll/student.html', {'stu' : stud})

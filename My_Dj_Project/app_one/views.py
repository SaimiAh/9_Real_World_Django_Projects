from django.shortcuts import render
from django.http import HttpResponse

def function_1(request):
    my_name = "Saim Ahmad"
    degree = "BSCS"
    sgpa = "3.6"
    details={'mn':my_name, 'deg':degree, 'gpa': sgpa, }
    return render(request,'index.html', context=details)
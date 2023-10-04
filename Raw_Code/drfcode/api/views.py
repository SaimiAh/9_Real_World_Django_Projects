from django.shortcuts import render
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def stucreate(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser.parse(stream)
        serializer = StudentSerializer(pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'message':'Data Created.', }
            json_data




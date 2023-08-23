from django.shortcuts import render
from .models import Students
from .serializer import Studentserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def student_del(request):
    student = Students.objects.all()
    print(student,'student')
    serializer = Studentserializer(student,many=True)
    print(serializer,'serializer')
    jsondata = JSONRenderer().render(serializer.data)
    return HttpResponse(jsondata, content_type='application/json')

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . models import Student

def index(request):
    return HttpResponse("Hello !!!! This is Views.")


def home(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render()) 


def simple(request):
    template = loader.get_template('mysecond.html')
    return HttpResponse(template.render())

def style(request):
    template = loader.get_template('mythird.html')
    return HttpResponse(template.render())

def student(request):
    mystudent = Student.objects.all().values()
    output = ""
    for x in mystudent:
        output += x["name"]
    return HttpResponse(output)

def add(request):
    template = loader.get_template('addstudent.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    x = request.POST['roll']
    y = request.POST['name']
    mystudent = Student(roll=x, name=y)
    mystudent.save()
    return HttpResponseRedirect(reverse(simple))

def showstudent(request):
    mystudent = Student.objects.all().values()
    template = loader.get_template('showstudent.html')
    context = { 'mystudent': mystudent,}
    return HttpResponse(template.render(context, request))

def addstudent(request):
    template = loader.get_template('studentform.html')
    return HttpResponse(template.render({},request))
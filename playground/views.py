import http
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# this is the request handler

def calculate():
    a = 1
    b = 2
    return 2

def say_hello(request):
    x = calculate()
    y = 2
    return render(request,'hello.html')
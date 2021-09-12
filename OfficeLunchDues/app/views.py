from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('hello worl welcome to app')

def next(request):
    return HttpResponse('hello worl welcome to app')
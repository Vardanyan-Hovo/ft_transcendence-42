from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def chat(request):
    return HttpResponse('<h1>Chat</h1>')
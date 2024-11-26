from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def NKR(request):
    return HttpResponse('<h1>NKR is a telugu boy</h1>')
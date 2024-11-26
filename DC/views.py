from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def david(request):
    return HttpResponse('he likes telugu film industry')
def warner(request):
    return HttpResponse('David warner')
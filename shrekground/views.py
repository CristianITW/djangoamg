from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request - response
#request handler
#action -> in Django: view

def say_shrek(request):
    #Pull data from DB
    #Transform data
    #Send Email
    return HttpResponse('Hello Shrek')
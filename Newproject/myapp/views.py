#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse("<h3>Welcome to my Website</h3>")




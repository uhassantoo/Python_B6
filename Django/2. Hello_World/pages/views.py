from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse('Hellow Python')

def about_view(request):
    return HttpResponse('About Page')
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  # return HttpResponse("Hello,World. You are at Manab Home page")
  return render(request,'website/index.html')

def about(request):
  return HttpResponse("Hello,World. You are at Manab About page")

def contact(request):
  return HttpResponse("Hello,World. You are at Manab Contact page")

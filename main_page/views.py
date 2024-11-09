from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Hello, my name is Elina!')
    
def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse("Hi! His name is Artsi. <img src='https://dk2dv4ezy246u.cloudfront.net/widgets/sSBDpovm7BA_large.jpg' />")

    
def system_time(request):
    if request.method == 'GET':
        current_time = datetime.now()  
        return HttpResponse(f"Current system time: {current_time}")
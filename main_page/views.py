from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models

def books_list_view(request):
    if request.method == 'GET':
        book_list = models.Books.objects.filter().order_by('-id')
        context = {'book_list': book_list}
        return render(request, template_name='book.html', context=context)

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        context = {'book_id': book_id}
        return render(request, template_name='book_detail.html', context=context)


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
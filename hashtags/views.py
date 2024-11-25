from django.shortcuts import render
from . import models

def all_clothes(request):
    if request.method == 'GET':
        clothes_list = models.Clothes.objects.filter().order_by('-id')
        context = {'clothes_list': clothes_list}
        return render(request, 'all.html',
                      context=context)

def older_list(request):
    if request.method == 'GET':
        older_list = models.Clothes.objects.filter(tags__name="For Olds").order_by('-id')
        context = {'older': older_list}
        return render(request, 'older.html',
                      context=context)

def younger_list(request):
    if request.method == 'GET':
        younger_list = models.Clothes.objects.filter(tags__name="For Young").order_by('-id')
        context = {'younger': younger_list}
        return render(request, 'younger.html',
                      context=context)
    
def kids_list(request):
    if request.method == 'GET':
        kids_list = models.Clothes.objects.filter(tags__name="For Kids").order_by('-id')
        context = {'kids': kids_list}
        return render(request, 'kids.html',
                      context=context)


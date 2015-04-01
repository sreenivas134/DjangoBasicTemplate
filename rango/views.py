from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    message = {'categories': category_list}
    
    return render(request, 'rango/index.html', message)

def about(sreenu):
    return render(sreenu, 'rango/about.html')

from django.shortcuts import render, redirect
from main import models


def home(request):
    """Home page"""
    categories = models.Category.objects.all()
    homes = models.Home.objects.all()[:9]
    context ={
        'categories': categories,
        'homes': homes,
    }
    return render(request, 'base.html', context)

def listing(request):
    """Listing page"""
    categories = models.Category.objects.all()
    homes = models.Home.objects.all()
    context ={
        'categories': categories,
        'homes': homes,
    }
    return render(request, 'houses/listing.html', context)

def detail(request, id):
    """Listing detail page"""
    homes = models.Home.objects.filter(id=id)
    context ={
        'homes': homes,
    }
    return render(request, 'houses/detail.html', context)
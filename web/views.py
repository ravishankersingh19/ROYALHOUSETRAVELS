from django.shortcuts import render

def index(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request,'about.html')


def news(request):
    return render (request,'news.html')

def contact(request):
    return render ('contact.html')


def destinations(request):
    return render ('destinations.html')


def elements(request):
    return render('elements.html')

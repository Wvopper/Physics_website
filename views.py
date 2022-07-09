from django.shortcuts import render, redirect


def index(request):
    data = {
        'title': 'The main page of the site'    
            }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def KinemBase(request):
    return render(request, 'main/KinemBase.html')

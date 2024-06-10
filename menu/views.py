from django.shortcuts import render

def index_view(request):
    return render(request, 'menu/index.html')

def about_view(request):
    return render(request, 'menu/about.html')

def cv_view(request):
    return render(request, 'menu/cv.html')

def other_view(request):
    return render(request, 'menu/other.html')

def tech_view(request):
    return render(request, 'menu/tech.html')
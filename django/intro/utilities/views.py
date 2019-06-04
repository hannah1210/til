from django.shortcuts import render

def index(request):

    return render(request, 'utilities/index.html')

def random_img(request):

    return render(request, 'utilities/random_img.html')

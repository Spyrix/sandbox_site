from django.shortcuts import render

# Create your views here.

def demo1(request):
    return render(request, 'demos/demo1.html', {'title': 'Demo1'})

def home(request):
    return render(request, 'demos/home.html',)

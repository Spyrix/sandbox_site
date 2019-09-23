from django.shortcuts import render


def home(request):
    return render(request, 'cs_review/home.html',)

def about(request):
    return render(request, 'cs_review/about.html', {'title': 'About'})

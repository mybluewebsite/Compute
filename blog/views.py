# myapp/views.py

from django.shortcuts import render

def home(request):
    context = {
        'page_title': 'My Awesome Django Project',
        'message': 'Welcome to your new Django application!',
    }
    return render(request, 'myapp/index.html', context)
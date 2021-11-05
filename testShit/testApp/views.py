from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    randoms = [
        {'title': 'Bitch'},
        {'title': 'Second Bitch'}
    ]
    return render(request, 'testApp/index.html', {
        'showM': True,
        'randoms': randoms
    })

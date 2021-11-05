from django.shortcuts import render
from django.http import HttpResponse

from .models import Jojo


# Create your views here.

def index(request):
    randoms = Jojo.objects.all()
    return render(request, 'testApp/index.html', {
        'randoms': randoms
    })


def details(request, shit_slug):
    try:
        selectedshit = Jojo.objects.get(slug=shit_slug)
        return render(request, 'testApp/details.html', {'selected': selectedshit, 'meetE': True})

    except Exception as exc:
        return render(request, 'testApp/details.html', {'meetE': False})

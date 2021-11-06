from django.shortcuts import render
from django.http import HttpResponse

from .models import Jojo
from .forms import RegistrarionForm


# Create your views here.

def index(request):
    randoms = Jojo.objects.all()
    return render(request, 'testApp/index.html', {
        'randoms': randoms
    })


def details(request, shit_slug):
    try:
        selectedshit = Jojo.objects.get(slug=shit_slug)
        registration_form = RegistrarionForm()
        return render(request, 'testApp/details.html', {'selected': selectedshit,
                                                        'meetE': True,
                                                        'form': registration_form})

    except Exception as exc:
        return render(request, 'testApp/details.html', {'meetE': False})

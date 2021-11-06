from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Jojo, Master
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
        if request.method == 'GET':
            registration_form = RegistrarionForm()

        else:
            registration_form = RegistrarionForm(request.POST)
            if registration_form.is_valid():
                emailU = registration_form.cleaned_data['email']
                master, _ = Master.objects.get_or_create(email=emailU)
                selectedshit.master.add(master)
                return redirect('confirm')

        return render(request, 'testApp/details.html', {'selected': selectedshit,
                                                        'meetE': True,
                                                        'form': registration_form})

    except Exception as exc:
        return render(request, 'testApp/details.html', {'meetE': False})


def confirm_req(request):
    return render(request, 'testApp/registrationSuc.html')

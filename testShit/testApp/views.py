from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    randoms = [
        {
            'title': 'Bitch',
            'location': 'Your Mama',
            'slug': 'Get-Fucket'},
        {
            'title': 'Bitch2',
            'location': 'Your Mama 2',
            'slug': 'Get-Fucket-2'}
    ]
    return render(request, 'testApp/index.html', {
        'showM': True,
        'randoms': randoms
    })


def details(request, shit_slug):
    selectedshit = {'title': 'This is shit', 'description': 'No Shit'}
    return render(request, 'testApp/details.html', {'selected': selectedshit})

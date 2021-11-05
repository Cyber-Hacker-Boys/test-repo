from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index, name='all'),
    path('test/<slug:shit_slug>', views.details, name='detail')
]
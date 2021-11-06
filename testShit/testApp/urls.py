from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all'),
    path('/success', views.confirm_req, name='confirm'),
    path('/<slug:shit_slug>', views.details, name='detail'),
]

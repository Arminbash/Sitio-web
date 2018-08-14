from django.urls import path

from .views import test

app_name = 'dashboard'

urlpatterns = [
    path('', test, name='index'),
]

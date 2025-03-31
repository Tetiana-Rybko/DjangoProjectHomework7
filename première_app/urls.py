from django.urls import path
from première_app.views import django_greetings

urlpatterns = [
    path('greetings/', django_greetings, name='django_greetings'),
]
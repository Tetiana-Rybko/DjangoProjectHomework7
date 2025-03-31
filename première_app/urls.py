from django.urls import path
from première_app.views import django_greetings, Salut_Rybka

urlpatterns = [
    path('greetings/', django_greetings, name='django_greetings'),
]
urlpatterns = [
    path('Salut/', Salut_Rybka, name='Salut_Rybka'),
]
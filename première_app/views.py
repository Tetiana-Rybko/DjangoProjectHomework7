from django.http import HttpResponse


def django_greetings(request):
    return HttpResponse("Hello, Tatiana")

# Create your views here.

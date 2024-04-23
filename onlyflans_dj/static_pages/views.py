from django.shortcuts import render
from .models import Flan

# Create your views here.
def index(request):
    flanes = Flan.objects.all()
    flanes_privados = Flan.objects.filter(is_private=True)
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {"flanes_publicos": flanes_publicos})

def about(request):
    return render(request, 'about.html', {})

def welcome(request):
    return render(request, 'welcome.html', {})
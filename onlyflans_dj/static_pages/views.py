from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactFormForm
from .models import Flan, ContactForm

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

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(** form.cleaned_data)
            return HttpResponseRedirect('/success')
        else: print("HUBO UN ERROR")
    else:
        form = ContactFormForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html', {})

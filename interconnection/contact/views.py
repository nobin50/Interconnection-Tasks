from django.shortcuts import render, redirect
from .models import Contact_List
from .forms import ContactForm

def contacts(request):
    contactAll = Contact_List.objects.all()
    context = {'contactAll': contactAll}

    return render(request, 'contact.html', context)


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.save()
        return redirect('contact')

    else:
        form = ContactForm

    return render(request, 'addContact.html', {'form': form})
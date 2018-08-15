from django.shortcuts import render
from .models import Contact_List

def contacts(request):
    contactAll = Contact_List.objects.all()
    context = {'contactAll': contactAll}

    return render(request, 'contact.html', context)

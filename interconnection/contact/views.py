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



def singleContact(request, contact_id):
    individualContact = Contact_List.objects.get(id = contact_id)
    contact = {'individualContact': individualContact}
    return render(request, 'singleContact.html', contact)



def edit_contact(request, contact_id):
    editContact = Contact_List.objects.get(id = contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=editContact)
        form.save()
        return redirect('contact')

    else:
        form = ContactForm(instance = editContact)

    return render(request, 'editContact.html', {'form': form})



def delete_contact(request, contact_id):
    delContact = Contact_List.objects.get(id=contact_id)
    delContact.delete()
    return redirect('contact')

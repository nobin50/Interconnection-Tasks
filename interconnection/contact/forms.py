from django import forms
from . models import Contact_List

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_List
        fields  = '__all__'

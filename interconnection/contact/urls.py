from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contacts, name="contact"),
    path('add-contact/', views.add_contact, name='addContact' ),
]
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contacts, name="contact"),
    path('add-contact/', views.add_contact, name='addContact' ),
    path('contact/<contact_id>/', views.singleContact, name='singleContact'),
    path('contact/<contact_id>/edit/', views.edit_contact, name='edit-contact'),
    path('contact/<contact_id>/delete/', views.delete_contact, name='delete-contact'),
]
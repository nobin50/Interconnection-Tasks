from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contact/$', views.ContactView.as_view()),
    url(r'^contact/(?P<pk>[0-9]+)/$', views.ContactDetailView.as_view())
]
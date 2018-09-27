from django.conf.urls import url, include
from rest_framework import routers
from . import views

todo_router = routers.DefaultRouter()
todo_router.register(r'todos', views.TodoViewSet, base_name='todos')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(todo_router.urls))
]

from django.urls import path
from .views import create_group
from . import views

urlpatterns = [
    path('group_creation/', views.create_group, name='group-creation'),
]


#  <app>/<model>_<viewtype>.html


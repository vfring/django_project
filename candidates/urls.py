from django.urls import path
from . import views

urlpatterns = [
    path('candidate_creation', views.candidateprofile, name='candidate-creation'),

]
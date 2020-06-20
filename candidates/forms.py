from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CandidateProfile



class CandidateProfUpdateForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['pimage','fir_name', 'las_name', 'run_party', 'cand_plat']
        labels = {
            'pimage': 'Picture for your candidacy',
            'fir_name': 'First Name',
            'las_name': 'Last Name',
            'run_party': 'What Party Are You A Part Of',
            'cand_plat': 'Enter your platform',


        }
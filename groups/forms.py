from .models import GroupCreation
from django import forms


class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = GroupCreation
        fields= [
            'group_name',
            'group_desc',
            'img_group',
                 ]
        labels = {
            'group_name': 'Group Name',
            'group_desc': 'Description',
            'img_group': 'Group Picture'
        }

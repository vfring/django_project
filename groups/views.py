from django.shortcuts import render, redirect
from .forms import GroupCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import Group
from .models import GroupCreation


@login_required
def create_group(request):
    if request.POST:
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            newGroup = form.save( commit=False)  #  commit=False gives you the model object and allows you to add your extra data and save it
            newGroup.author = request.user       # insert line of code that checks if name has already been taken
            newGroup.date_posted = timezone.now

            newGroup.save()

            g1 = Group.objects.create(name=newGroup.group_name)

            g1.user_set.add(newGroup.author)

            print(newGroup)

    else:
        form = GroupCreationForm()

    context = {'form': form}

    return render(request, "groups/group_creation.html", context)

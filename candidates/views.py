from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CandidateProfUpdateForm

@login_required
def candidateprofile(request):
    if request.method == 'POST':
        form = CandidateProfUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have created a new organization!')
            return redirect('profile')      # link this to "candidate view page

    else:
        form = CandidateProfUpdateForm()

    context = {
        'form': form,
    }

    return render(request, 'candidates/candidate_creation.html', context)



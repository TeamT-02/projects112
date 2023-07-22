from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from eng.models import UserCreateForm


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('index')
    else:
        form = UserCreateForm()

    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)



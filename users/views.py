from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from users.forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return redirect('main')
        
    else:
        form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('users:login')
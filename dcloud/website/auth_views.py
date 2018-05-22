from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def delete_account(request):
    if request.method == 'GET':
        return render(request, 'registration/delete_account.html')
    elif request.method == 'POST':
        if request.POST.get('yes'):
            return redirect('delete_account_success')
        else:
            return redirect('/')

@login_required
def delete_account_success(request):
    if request.method == 'GET':
        # TODO Add delete account
        return render(request, 'registration/delete_account_success.html')


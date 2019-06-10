from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())

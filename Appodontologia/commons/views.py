
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages


# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context,request))


def login_and_register(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        register_form = UserCreationForm(request.POST)

        if 'login' in request.POST and login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')  # Cambia 'dashboard' por la URL de tu página principal después de iniciar sesión
            else:
                messages.error(request, 'Invalid username or password.')

        elif 'register' in request.POST and register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login_and_register')  # Cambia 'login_and_register' por la URL de tu página de inicio de sesión y registro

    else:
        login_form = AuthenticationForm()
        register_form = UserCreationForm()

    return render(request, 'commons/login_and_register.html', {'login_form': login_form, 'register_form': register_form})
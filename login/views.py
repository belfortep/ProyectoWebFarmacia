from django.shortcuts import render, redirect
from .forms import FormularioLogin
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.


def login(request):

    formulario_login=UserRegisterForm()
    return render(request, 'login/login.html', {'form' : formulario_login})


    



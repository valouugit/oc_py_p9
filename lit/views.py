from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest

from lit.form.register import RegisterForm


def register(request: WSGIRequest):
    if request.method == 'POST':
        register = RegisterForm(request.POST)
        if register.is_valid():
            register.save()
            return redirect("/")

    return render(request, "registration/register.html", context={"form":RegisterForm})

@login_required
def index(request):
    return render(request, "lit/index.html")

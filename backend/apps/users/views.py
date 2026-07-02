from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("core:home")
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("core:home")
    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("core:home")
from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)

            login(request, user)
            messages.success(
                request,
                "Registration was successful",
                extra_tags="alert alert-success alert-dismissible fade show",
            )
            return redirect("/")
    else:
        form = UserRegistrationForm()
    return render(request, "auth/signup.html", {"form": form})


def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.error(
                    request,
                    "Check your login details and try again",
                    extra_tags="alert alert-danger alert-dismissible fade show",
                )
                return redirect("/")

    return render(request, "auth/login.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("login")

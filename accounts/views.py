from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.

def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect("/")
    context = {
        "form": form,
        "btn": "Login",
        "title": "Login",
        }
    return render(request, "accounts/login.html", context)

def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    context = {
        "form": None,
        "btn": "Logout",
        "title": "Logout",
        }
    return render(request, "accounts/logout.html", context)

def register_view(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    context = {
        "form": form,
        "btn": "Register",
        "title": "Register",
    }
    return render(request, "accounts/register.html", context)
        

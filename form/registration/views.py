# registration/views.py

from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from .forms import RegistrationForm


def register(request):
    try:
        template = get_template("registration/register.html")
    except Exception as e:
        return HttpResponse(f"Template loading error: {e}")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})


def success(request):
    return render(request, "registration/success.html")


# from django.shortcuts import render, redirect
# from .forms import RegistrationForm


# def register(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("success")
#     else:
#         form = RegistrationForm()
#     return render(request, "/registration/register.html", {"form": form})


# def success(request):
#     return render(request, "/registration/success.html")

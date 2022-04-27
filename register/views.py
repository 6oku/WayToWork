from re import template
from django.shortcuts import render, redirect
from .forms import RegisterForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

"""
def register(response):
	if response.method == 'POST':
		form = RegisterForm(response.POST)
		if form.is_valid():
				form.save

		return redirect("/login")
	else:
		form = RegisterForm()

	return render(response, "register/register.html", {"form":form})
"""


def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/todo")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegisterForm()
	return render(request=request, template_name="register/register.html", context={"form":form})
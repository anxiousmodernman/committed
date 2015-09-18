from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "user/home.html")


def github_login_fail(request):
    return HttpResponse("Login with GitHub failed.")

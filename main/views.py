from django.shortcuts import render
from committed import settings
from django.shortcuts import redirect

# Create your views here.


def hello(request):
    return render(request, "main/home.html")  # todo you can give a context here


def github_login(request):
    return render(request, "main/home.html")


def logout(request):
    logout(request)
    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
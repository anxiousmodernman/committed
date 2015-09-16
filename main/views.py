from django.shortcuts import render
from committed import settings
from django.shortcuts import redirect

# Create your views here.


def hello(request):
    return render(request, "main/begin.html")  # todo you can give a context here


def logout(request):
    logout(request)
    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
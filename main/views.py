from django.shortcuts import render

# Create your views here.


def hello(request):
    return render(request, "main/home.html")  # todo you can give a context here


def github_login(request):
    pass
    return render(request, "main/home.html")


def logout(request):
    # return HttpResponse("Thanks for logging out")
    pass
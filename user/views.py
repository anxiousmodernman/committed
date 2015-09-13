from django.http import HttpResponse


def home(request):
    return HttpResponse("You have successfully logged in somehow.")


def github_login_fail(request):
    return HttpResponse("Login with GitHub failed.")

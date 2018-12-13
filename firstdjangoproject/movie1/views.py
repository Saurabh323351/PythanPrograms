from django.http import HttpResponse


def index(request):
    return HttpResponse("<h7> Hello Saurabh Singh</h7>")


def letsee(request):
    return HttpResponse("<h1>hi</h1>")


def company_details(request):
    return HttpResponse("<h3> Hi its happening </h3>")

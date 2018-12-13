from django.http import HttpResponse


def another(request):
    return HttpResponse("<h1> Is it executing ie movie2</h1>")

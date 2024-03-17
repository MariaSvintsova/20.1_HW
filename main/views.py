from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет, мир! Это мое первое представление Django.")

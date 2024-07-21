from django.http import HttpResponse
def home_simple(request):
    return HttpResponse("Welcome to the Home Page!")
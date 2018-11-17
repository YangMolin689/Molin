from django.http import HttpResponse

def index(request):
    return HttpResponse('HELLO')

def login(request):
    return HttpResoponse('666')

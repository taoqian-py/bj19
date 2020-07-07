import django.http from HttpResponse


def index(request):
	return HttpResponse('/index')

from django.http import HttpResponse

def home(request):
	return HttpResponse("Car Database Management System")
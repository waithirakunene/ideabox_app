from django.shortcuts import render
from django.http import HttpResponse
from .models import Ideas


# Create your views here.
def home(request):
	context = {
	'ideabox': Ideas.objects.all()
	}
	return render(request, 'ideabox/home.html',context)


def about(request):
	return render(request, 'ideabox/about.html')

#from django.http import HttpResponse




	
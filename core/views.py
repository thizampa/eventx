# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, Context
from django.template import RequestContext

def homepage(request):
	return HttpResponse('Bem vindo ao Eventex')
	


def homepage(request):
	t = loader.get_template('index.html')
	c = Context()
	
	content = t.render(c)
	
	return HttpResponse(content)
	

def homepage(request):
	return render_to_response('index.html')


def homepage(request):
	from django.conf import settings
	context = {'MEDIA_URL': settings.MEDIA_URL}
	return render_to_response('index.html', context)


def homepage(request):
	context = RequestContext(request)
	return render_to_response('index.html', context)
from django.shortcuts import render

#using generics
from django.views.generic import TemplateView

# Create your views here.

class BaseView(TemplateView):
	template_name = 'base.html'

class port1View(TemplateView):
	template_name = 'port1.html'

class port2View(TemplateView):
	template_name = 'port2.html'

class port3View(TemplateView):
	template_name = 'port3.html'

class port4View(TemplateView):
	template_name = 'port4.html'

class port5View(TemplateView):
	template_name = 'port5.html'

class port6View(TemplateView):
	template_name = 'port6.html'
from django.shortcuts import render

#using generics
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
	template_name = 'home.html'
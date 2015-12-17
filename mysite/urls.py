"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from mainsite.views import BaseView
from mainsite.views import port1View, port2View, port3View, port4View, port5View, port6View

urlpatterns = [
	url(r'^$', BaseView.as_view(), name ='base'),
	url(r'^port1/$', port1View.as_view(), name = 'port1'),
    url(r'^port2/$', port2View.as_view(), name = 'port2'),
    url(r'^port3/$', port3View.as_view(), name = 'port3'),
    url(r'^port4/$', port4View.as_view(), name = 'port4'),
    url(r'^port5/$', port5View.as_view(), name = 'port5'),
    url(r'^port6/$', port6View.as_view(), name = 'port6'),
    url(r'^admin/', include(admin.site.urls)),
]


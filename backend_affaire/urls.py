#-*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^formulaire$', views.formulaire),
]

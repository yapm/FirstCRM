#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """

    text = """
    <h1>This is the backend homepage</h1>
    <p>This is an access to the backend for the CRM of iXblue</p>
             """
    return HttpResponse(text)

def formulaire(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """

    text = """
    <h1>This is the formulaire page</h1>
    <p>This is an access to the formulaire for the CRM of iXblue</p>
             """
    return HttpResponse(text)

#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    type_produit = models.CharField(max_length=70, null=True)
    description = models.TextField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date of creation")

    def __str__(self):
        """
        permet de reconnaître les différents modèles dans l'administration
        """
        return self.name

def __unicode__(self):
    return self.name

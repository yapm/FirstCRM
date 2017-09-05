#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Bid(models.Model):
    affair_number = models.CharField(max_length=10, null=True, blank=True, unique=True)
    project_price = models.DecimalField(max_digits=13, decimal_places=2, verbose_name="Price of the project", null = True)
#    customer = models.ForeignKey('Customer', verbose_name = "Customer")
#    final_customer = models.ForeignKey('Customer', verbose_name = "Final Customer")
#    shipyard = models.ForeignKey('Customer', verbose_name = "Shipyard")
#    seller = models.ForeignKey('Seller', verbose_name = "Seller")
#    scope_supply = models.ForeignKey('ScopeSupply', verbose_name = "Scope of Supply")

    def __str__(self):
        """
        permet de reconnaître les différents modèles dans l'administration
        """
        return self.affair_number

    def __unicode__(self):
       return self.affair_number

class Person(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    trigramme = models.CharField(max_length=4, null=True, blank=True)

    class meta:
        abstract = True

    def __str__(self):
        """
        permet de reconnaître les différents modèles dans l'administration
        """
        return self.name

    def __unicode__(self):
       return self.name

class Seller(Person):
   region_allocated =  models.CharField(max_length=255, null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    type_produit = models.CharField(max_length=70, null=True)
    price_std = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Standard price", null = True)
    ax_cost = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Cost in AX", null = True)
    description = models.TextField(null=True)

#    class meta:
#        abstract = True
#Cette base sert de skelette mais aussi pour définir les produits de base
    def __str__(self):
        """
        permet de reconnaître les différents modèles dans l'administration
        """
        return self.name

    def __unicode__(self):
       return self.name

class ProductProject(Product):
    bid_project = models.ForeignKey('Bid', null = True)
    cost_project = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Project cost", null = True)
    price_quotation = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Price quotation", null = True)

class CompositionNetans(ProductProject):
    nb_mod_rs422 = models.PositiveSmallIntegerField(null = True)
    nb_mod_synchro = models.PositiveSmallIntegerField(null = True)
    nb_mod_ntds= models.PositiveSmallIntegerField(null = True)

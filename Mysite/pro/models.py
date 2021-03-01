from django.db import models
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django.urls import reverse
from mapbox_location_field.models import LocationField





class Clients (models.Model):
    région = models.ForeignKey('Location', on_delete=models.CASCADE, default='true')
    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    wilaya = models.ForeignKey('Wilaya', on_delete=models.SET_NULL, null=True)
    localité = models.CharField(max_length=255)
    nom_gérant = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    téléphone = models.CharField(max_length=255)
    potentiel = models.CharField(max_length=255)
    distributeur = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
    class Meta:
        ordering = ["-id"]

class Location (models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom



class Produit (models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

    ordering = ["-id"]

class Wilaya (models.Model) :
    région = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Localité (models.Model) :
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name



class Bc (models.Model):
    client = models.ForeignKey('Clients', null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "#BC_"+ str(self.id)

    class Meta:
        ordering = ["-id"]


class Order (models.Model):
    bc = models.ForeignKey('Bc', null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey('Clients', null=True, on_delete=models.SET_NULL)
    designation = models.ForeignKey('Produit',null=True, on_delete=models.SET_NULL)
    quantité_disponible = models.IntegerField()
    commande = models.IntegerField()
    description = models.CharField(max_length=255)
    disponibilité_concurrent = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, null=True)
    créer_par = CurrentUserField()

    class Meta:
        ordering = ["-date"]





class Visite_test (models.Model):

    Titre = models.CharField(max_length=255)
    région = models.ForeignKey(Location, on_delete=models.CASCADE)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.SET_NULL, null=True)
    localité = models.ForeignKey(Localité, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=255)
    localisation = LocationField(null=True)
    date = models.DateField(null=True)

    status_choice = (
        ('En cours', 'En cours'),
        ('Annulée', 'Annulé'),

        ('Changée', 'Changé'),
        ('Cloturée', 'Cloturé'),
    )
    status = models.CharField(choices=status_choice, max_length=10)




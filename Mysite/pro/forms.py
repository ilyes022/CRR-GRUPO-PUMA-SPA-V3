from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Fieldset, HTML, ButtonHolder, Submit
from django import forms

from .models import   Clients, Location, Produit, Wilaya, Order, Visite_test, Bc, Localité
from django import forms
from django.forms import ModelChoiceField, ModelForm, DateInput, inlineformset_factory,modelformset_factory
from django.db.models import F
from datetimepicker.widgets import DateTimePicker
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.utils import timezone
from django.utils import formats, translation
from django.contrib.admin import widgets


class BcForm(ModelForm):
    class Meta:
        model = Bc
        fields = ['client']




class Loginform(forms.Form):
    username= forms.CharField(max_length= 25,label="Username")
    password= forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)







choix2 = [
    ('..', '..'),
    ('oui', 'Oui'),
    ('non', 'Non'),
]



class RowProduitsForm(forms.Form):
    date = forms.DateField(help_text="Please use the following format: <em>Mois/Jour/Année</em>.")
    client = forms.ModelChoiceField(queryset=Clients.objects.all())
    région = forms.ModelChoiceField(queryset=Location.objects.all())
    wilaya = forms.ModelChoiceField(queryset=Wilaya.objects.all())
    #designation = forms.ModelChoiceField(queryset=Produit.objects.all())
    #disponibilité = forms.CharField(widget=forms.Select(choices= choix2))
    #quantité_disponible = forms.IntegerField()
    #commande = forms.IntegerField()
    #description = forms.CharField(widget=forms.Textarea, required= False)
    #disponibilité_concurrent = forms.CharField(widget=forms.Select(choices= choix2))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wilaya'].queryset = Wilaya.objects.none()

        if 'région' in self.data:
            try:
                région_id = int(self.data.get('région'))
               #self.fields['wilaya'].queryset = Wilaya.objects.filter(région_id=région_id).order_by('name')

            except (ValueError, TypeError):
               pass   #invalid input from the client; ignore and fallback to empty City queryset
        #elif self.instance.pk:
            #self.fields['wilaya'].queryset = self.instance.région.wilaya_set.order_by('name')







class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = [
            'région',
            'nom',
            'type',
            'wilaya',
            'localité',
            'nom_gérant',
            'adresse',
            'téléphone',
            'potentiel',
            'distributeur',
        ]
type_client = [
    ('..','..'),
    ('ceramiste', 'Ceramiste'),
    ('materiaux de construction', 'Materiaux De Construction'),
    ('quincaillerie', 'Quincaillerie'),

]
#wiliya_client = [
    #('..','..'),
    #('alger', 'Alger'),
    #('oran', 'Oran'),

#]
localité_client = [

    ('..','..'),
    ('belarbi', 'Belarbi'),
    ('ben badis', 'Ben Badis'),

]
potentiel_client = [
    ('..','..'),
    ('fort','Fort'),
    ('moyen','Moyen'),
    ('faible','Faible'),
]

distributeur_client = [
    ('..','..'),
    ('bs mat','Bs Mat'),
    ('bouali','Bouali'),

]
type_location = [
    ('centre','Centre'),
    ('est','Est'),
]

class RowClientsForm(forms.Form):
    région = forms.ModelChoiceField(queryset=Location.objects.all())
    nom = forms.CharField()
    type = forms.CharField(widget=forms.Select(choices= type_client))
    wilaya = forms.ModelChoiceField(queryset=Wilaya.objects.all())
    localité = forms.ModelChoiceField(queryset=Localité.objects.all())
    nom_gérant = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    téléphone = forms.IntegerField()
    potentiel = forms.CharField(widget=forms.Select(choices= potentiel_client))
    distributeur = forms.CharField(widget=forms.Select(choices= distributeur_client))


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'nom',
        ]




###########################################################################################




##################################################################################

class OrderForm(ModelForm):

	class Meta:
		model = Order
		fields = '__all__'

#################################################################################

class Visite_testForm(forms.ModelForm):


  class Meta:
    model = Visite_test
    fields = ['Titre','région','wilaya','localité','description','localisation','date','status']
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
        'date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),

    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wilaya'].queryset = Wilaya.objects.none()

        if 'région' in self.data:
            try:
                région_id = int(self.data.get('région'))
               #self.fields['wilaya'].queryset = Wilaya.objects.filter(région_id=région_id).order_by('name')

            except (ValueError, TypeError):
               pass   #invalid input from the client; ignore and fallback to empty City queryset
        #elif self.instance.pk:
            #self.fields['wilaya'].queryset = self.instance.région.wilaya_set.order_by('name')


  #def __init__(self, *args, **kwargs):
    #super(Visite_testForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    #self.fields['start_time'].input_formats = ('%Y-%m-%d',)
    #self.fields['end_time'].input_formats = ('%Y-%m-%d',)







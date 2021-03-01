import django_filters
from .models import  Clients, Order, Visite_test, Bc
from django_filters import DateFilter


class PumalFilter(django_filters.FilterSet):
    date_début = DateFilter(field_name='date', lookup_expr='gte', label='Date début')

    date_fin = DateFilter(field_name='date', lookup_expr='lte', label='Date Fin')



    class Meta:
        model = Order
        fields = ['bc__client','bc__client__région', 'designation']



class ClientsFilter(django_filters.FilterSet):
    class Meta :
        model = Clients
        fields = ['nom','région','wilaya']

class NumberFilter(django_filters.FilterSet):

    class Meta:
        model = Order

        fields = {
           'date': ['month'],
       }


class NumberFilter2(django_filters.FilterSet):
    class Meta:
        model = Visite_test

        fields = {
            'date': ['month'],
        }


class Number_Filter3(django_filters.FilterSet):
    class Meta:
        model = Bc

        fields = {
            'date': ['month'],
        }




class Visite_testFilter(django_filters.FilterSet):
    class Meta :
        model = Visite_test
        fields = ['région','wilaya','date','status']

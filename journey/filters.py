import django_filters as filters
from .models import City,Persons,Country,Turn

class TurnFilter(filters.FilterSet):
    price = filters.NumberFilter('price','range')
    city = filters.ModelChoiceFilter(queryset=City.objects.all(),empty_label='Hamisi')
    country = filters.ModelChoiceFilter(queryset=Country.objects.all(),empty_label='Hamisi')
    class Meta:
        model = Turn
        fields = ['price','city','country']
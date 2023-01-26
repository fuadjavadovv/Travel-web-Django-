from rest_framework import serializers
from journey.models import Turn,Country,City
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CountrySerializers(serializers.ModelSerializer):
     class Meta:
        model = Country
        fields = ['name']

class CitySerializers(serializers.ModelSerializer):
     class Meta:
        model = City
        fields = ['name']


class TurnSerializer(serializers.ModelSerializer):
    persons = UserSerializers(many=True)
    country = CountrySerializers()
    city = CitySerializers()
    class Meta:
        model = Turn
        fields = ['name','country','city','description','start_date','finsh_date','img','price','daysall','max_person','persons']
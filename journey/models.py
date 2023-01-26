from django.db import models
from django.db.models import Count

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
class Country(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Persons(models.Model):
    user=models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.user



class Turn(models.Model):
    created_user = models.ForeignKey(User,on_delete = models.CASCADE, related_name='turns')
    name = models.CharField(max_length = 250)
    # country = models.CharField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add= False)
    finsh_date = models.DateTimeField(auto_now_add=False)
    img = models.ImageField()
    price = models.IntegerField()
    daysall = models.IntegerField()
    max_person = models.IntegerField() 
    persons = models.ManyToManyField(User,related_name="person_turns")
    longitude = models.CharField(max_length=100, null=True, blank=True)
    lattitude = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(blank=True,unique=True)
    # hostname=models.CharField(max_length=150,blank=True,null=True)
    # ip_address=models.GenericIPAddressField()
    def __str__(self):
        return self.name
    

    def get_main_count(self):
        maxx = self.max_person
        turn = self.persons.count()
   
        
      

        return maxx-turn


    # def __str__(self):
    #     return self.name



    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    # def get_main_emptyperson(self):
    #     self.max_person - 



class Reservation(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    turn = models.ForeignKey(Turn,on_delete=models.SET_NULL,null=True,related_name='firstturn')
    name = models.CharField(max_length = 250) 
    mail = models.EmailField()
    # number = models.CharField(max_length = 250)
    # age = models.IntegerField()
    
    def __str__(self):
        return str(self.age)


from django.contrib import admin
from journey.models import City,Country,Turn,Persons,Reservation
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)
# Register your models here.
class TurnAdmin(admin.ModelAdmin):
   list_display = ['name','country','price','created_user','city','id']
   search_fields = ['name']
   list_filter = (('price',DropdownFilter),)
   list_select_related = ['created_user']


admin.site.register(Turn,TurnAdmin)
 


admin.site.register(City)
admin.site.register(Country)
admin.site.register(Persons)
admin.site.register(Reservation)
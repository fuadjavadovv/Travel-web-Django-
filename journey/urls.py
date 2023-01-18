
from xml.etree.ElementInclude import include
from django.urls import path
from journey import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('deals/', views.deals, name="deals"),
    path('travel/<int:id>/', views.travel_detail, name="travel_detail"),
    # path('travel/reservation/', views.travel_reserv, name="travel_reservation"),
    path('enroll_the_course/', views.enroll_the_course, name="enroll_the_course"),
    path('travel_register/', views.travel_register, name="travel_register"),

]

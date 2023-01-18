
from xml.etree.ElementInclude import include
from django.urls import path
from user import views

urlpatterns = [
    
    path('login/', views.login_page, name="loginn"),
    path('register/', views.register_page, name="registerr"),
    path('logout/', views.logout_page, name="logout"),

]

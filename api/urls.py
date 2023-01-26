
from django.urls import path, include
from api import views as api_views

urlpatterns = [
    path('turn/',api_views.TurnListCreateAPIView.as_view(), name = 'turn' ),
    path('country/',api_views.CountryistCreateAPIView.as_view(), name = 'country' ),
    path('turn/<int:turn_pk>/join/',api_views.join_enter,name='join'),
    path('turn/<int:turn_pk>/quit/',api_views.quit,name='quit'),
    path('city/',api_views.CityistCreateAPIView.as_view(), name = 'city' ),
  


] 

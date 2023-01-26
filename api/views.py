from rest_framework import generics
from journey.models import Turn,City,Country
from django.shortcuts import render
from .serializers import CountrySerializers,CitySerializers,TurnSerializer
from .pagination import Turnpagination
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, parsers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .permissions import TurnPermission

class TurnListCreateAPIView(generics.ListCreateAPIView):
    queryset = Turn.objects.all()
    serializer_class = TurnSerializer
    pagination_class = Turnpagination

class CountryistCreateAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers


class CityistCreateAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializers


@api_view(['GET'])    
@permission_classes([TurnPermission])
def join_enter(request,turn_pk):
    # statuss = 'Ugurlu!'
    author = request.user
    turn = get_object_or_404(Turn,pk=turn_pk)
    print("ffffffffffffffffffhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhffffffff")
    if author in turn.persons.all():
          return Response({"Success": "Qeyd OLunub"},status=status.HTTP_202_ACCEPTED) 

    if turn.max_person > turn.persons.count():
     turn.persons.add(author)
     return Response({"Succ":"Ugurlu"},status = status.HTTP_400_BAD_REQUEST)

    else:
             return Response({"Warning":"Artiq Doludur"},status = status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])    
def quit(request,turn_pk):
    author = request.user
    turn = get_object_or_404(Turn,pk=turn_pk)
    if author in turn.persons.all():
          turn.persons.remove(author)
          return Response({"Success": "Artiq cixis oldunuz"},status=status.HTTP_202_ACCEPTED)

    else:
          return Response({"Success": "Cis olunmaqiniza ehtiyac yoxdur cunki siyahida yoxsunuz"},status=status.HTTP_302_FOUND)



    
 

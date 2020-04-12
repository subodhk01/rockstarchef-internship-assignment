from rest_framework import viewsets, filters, generics
from .models import *
from .serializers import *

from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

class CsrfExemptSessionAuthentication(SessionAuthentication):    # To remove the csrf check
    def enforce_csrf(self, request):
        return  

class MovieViewset(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    search_fields = ['name','rating']            # Can be changed according to use
    filter_backends = (filters.SearchFilter, )
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
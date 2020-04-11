from rest_framework import viewsets
from .models import *
from .serializers import *

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
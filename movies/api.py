from rest_framework import routers
from main import api_views

router = routers.DefaultRouter()
router.register(r'movies', api_views.MovieViewset ) 
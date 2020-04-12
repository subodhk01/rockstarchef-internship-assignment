from django.contrib import admin
from django.urls import path, include
from .api import router
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('user/login', views.user_login),
    path('user/signup', views.user_register),
    path('user/logout', views.user_logout),
]

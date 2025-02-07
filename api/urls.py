# 
#
#from django.urls import path, include
#from api import views
#
#urlpatterns = [
#    path('', views.index, name="index"),
#]

# esta es la forma de crear la ruta con django frest framework
from rest_framework import routers
from .api import ApiViewSet

ruta = routers.DefaultRouter()
ruta.register('api/empleados', ApiViewSet, 'api')

urlpatterns = ruta.urls



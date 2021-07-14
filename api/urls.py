from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
# from django.urls import include, path

# from rest_framework.routers import DefaultRouter

# from .views import (

# )

# router = DefaultRouter()
# router.register(

# )

# urlpatterns = [
#     path('', include(router.urls)),
# ]
# urlpatterns += [

# ]
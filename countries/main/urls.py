from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.about),
    path('countries', views.countries_list, name='country'),
    path('languages', views.languages_list, name='language'),
    path('countries/<id_country>', views.countries_index),
    path('languages/<id_language>', views.languages_index),
]
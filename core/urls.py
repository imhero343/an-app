from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.tech, name='tech'),
    path('tech/ajax/', views.techAjax, name='techajax'),
    path('done/', views.done, name='done'),



]

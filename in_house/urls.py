from unicodedata import name
from django.urls import path
from . import views 

urlpatterns = [
path('',views.index, name="in_house"),
path('offloaded/',views.ofloadedCargo,name="offloaded"),
]
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.trackFinance ,name='track-finance'),
]
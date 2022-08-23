from django.urls import path
from . import views 

urlpatterns = [
    # path to trackfinance ``.
    path('',views.trackFinance ,name='track-finance'),
]
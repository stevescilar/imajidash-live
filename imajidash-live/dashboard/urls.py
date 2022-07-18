from unicodedata import name
from django.urls import path
from . import views 
urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('register/',views.registerPage,name="register"),
    path('logout/',views.logoutUser,name="logout"),

    path('',views.index, name="dashboard"),
    path('chart/',views.chart,name='chart'),
    path('client/',views.client,name='client'),
    path('agent/',views.agent,name='agent'),
    path('sales-agent/',views.createSalesAgent,name='sales-agent'),
    # cargo logistics ^ operations
    # Guangzhou
    path('receive-china/',views.receiveChina,name='receive-china'),
    path('dispatch-china/',views.dispatchChina,name='dispatch-china'),
    path('dispatched-china/',views.dispatchedChina, name='dispatched-china'),
    path('china/', views.china , name='china'),
    # Yiwu
    path('yiwu/', views.yiwu , name='yiwu'),
    path('receive-yiwu/',views.receiveYiwu,name='receive-yiwu'),
    path('dispatch-yiwu/',views.dispatchYiwu,name='dispatch-yiwu'),
    path('dispatched-yiwu/',views.dispatchedYiwu, name='dispatched-yiwu'),


    # kENYA
    path('receive-kenya/',views.receiveKenya,name='receive-kenya'),
    path('dispatch-kenya/',views.dispatchKenya,name='dispatch-kenya'),
    path('dispatched-kenya/',views.dispatchedKenya, name='dispatched-kenya'),
    path('create-client/',views.createClient, name = 'create-client'),
    path('create-remark/',views.createRemark, name = 'create-remark'),
    path('remark<str:pk>/', views.remark , name = 'remark'),
    path('kenya/', views.kenya , name='kenya'),
    

    # search
    path('search/', views.search, name = 'search'),
    path('searchAdd/', views.searchAdd, name = 'searchAdd'),

]
    


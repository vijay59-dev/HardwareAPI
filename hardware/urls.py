from django.urls import path

from hardware import views

urlpatterns = [

       path('', views.home, name='homescreen'),
       path('cpu/', views.cpuDetails, name='cpuDetails'),
       path('disk/', views.diskDetails, name='diskDetails'),
       path('ram/', views.ramDetails, name='ramDetails'),
       path('battery/', views.batteryDetails, name='batteryDetails'),
]
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('upload_csv',views.upload_csv),
    path('open_csv',views.open_csv),
    # path('read',views.readcsv)
]
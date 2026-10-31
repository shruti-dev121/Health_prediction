from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('index/',views.index ),
    path('creates/',views.creates,name='creates'),
    path('', views.index, name='index'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]

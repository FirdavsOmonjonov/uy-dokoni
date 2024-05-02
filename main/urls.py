from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home_page'),
    path('listing/', views.listing, name='listing'),
    path('detail/<int:id>/', views.detail, name='detail'),
]
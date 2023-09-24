from django.urls import path
from . import views

urlpatterns = [
    path('one/', views.one, name='index'),
    path('two/', views.two, name='two'),
    path('three/', views.three, name='three'),
]

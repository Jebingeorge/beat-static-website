from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('booking', views.booking, name='booking'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact')
]
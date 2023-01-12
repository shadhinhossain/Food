from django.urls import path
from user import views




urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('events', views.events, name='events'),
    path('chefs', views.chefs, name='chefs'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),

    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('register', views.register, name='register'),
]

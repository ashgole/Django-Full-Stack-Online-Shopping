from django import urls
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('forget/', views.forget),
    path('password/post', views.setPassword),

    path('home/', views.home),
    path('home/<id>', views.getProduct),
    path('postSignin/', views.postSignin),
    path('buy/', views.postBuy),

    path('cart/', views.getCart),
    path('postcart/', views.postCart),
    path('deletecart/', views.deleteCart),

    path('profile/', views.getProfile),
    path('profile/edit/<username>', views.getPutProfile),
    path('profile/edit2/', views.putProfile),

]
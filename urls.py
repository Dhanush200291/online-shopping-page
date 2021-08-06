from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='napster'),
    path('register',views.register,name='napster'),
    path('home',views.home,name='napster'),
    path('signin',views.signin,name='napster'),

]
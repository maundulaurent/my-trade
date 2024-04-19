from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('demo', views.demo, name="demo"),
    path('signup', views.signup, name="signup"),
    path('login', views.my_login, name='login'),
    path('login', views.my_login, name='login'),
    path('logout',views.my_logout,name='logout'),
]
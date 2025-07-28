from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('codesence', views.codesence, name='codesence'),
    path('shop', views.shop, name='shop'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'), 
    path('signup', views.signup, name='signup'),



    #Additional Pages
    path('front', views.front, name='front'),
    path('back', views.back, name='back'),
    path('software', views.software, name='software'),
    path('database', views.database, name='database'),
]
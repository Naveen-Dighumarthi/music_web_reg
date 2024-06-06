from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.home,name='index'),
     path('signup/',views.signup,name='signup'),
      path('login/',views.custom_login,name='signup'),
]




from django.urls import path
from . import views

urlpatterns = [
    path('', views.settings_gen, name='main-page'),
    path('password', views.generate_password, name='pswrd'),
    path('about', views.about, name='about'),
]
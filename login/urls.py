from django.contrib import admin
from django.urls import path,include

from . import views

app_name = 'login'
urlpatterns = [
    path('',views.login,name = 'login'),
    path('login_submission',views.request,name ='login_submission')
]

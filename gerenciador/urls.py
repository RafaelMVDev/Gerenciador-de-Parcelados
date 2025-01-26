from django.urls import path
from . import views

urlpatterns= [
    path('',views.start_page, name="home"),
    path('next',views.next_page,name="next")
]
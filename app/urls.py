from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('hien_thi', views.hien_thi,name="show"),
]
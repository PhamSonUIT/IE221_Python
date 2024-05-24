from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('hien_thi_nv/', views.hien_thi_nv,name="hien_thi_nv"),
    path('them_nv/', views.them_nv,name="them_nv"),
]
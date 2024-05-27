from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('hien_thi_nv/', views.hien_thi_nv,name="hien_thi_nv"),
    path('them_nv/', views.them_nv,name="them_nv"),
    path('xoa_nv/<int:ma_nv>/', views.xoa_nv, name="xoa_nv"),
    path('cap_nhat_nv/<int:ma_nv>/', views.cap_nhat_nv, name="cap_nhat_nv"),
    path('tinh_luong/<str:ma_nv>/', views.tinh_luong, name="tinh_luong"),  

]
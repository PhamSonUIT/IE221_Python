from django.shortcuts import render
from django.http import HttpResponse
from .models import NhanVien

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def hien_thi(request):
    ds_nv = NhanVien.objects.all()
    return render(request, 'app/hien_thi_nv.html', {'nv':ds_nv})

def liet_ke_nv(requets):
    ds_nv = NhanVien.objects.all()
    output = "</br>".join([nv.ho_ten for nv in ds_nv])
    return HttpResponse(output)
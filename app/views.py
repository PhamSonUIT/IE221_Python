from django.shortcuts import render
from django.http import HttpResponse
from .models import NhanVien

# Create your views here.
def home(request):
    return render(request, 'app/home.html')
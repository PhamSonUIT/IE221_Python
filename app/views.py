from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import NhanVien

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def tinh_luong(request, ma_nv):
    nhan_vien = get_object_or_404(NhanVien, ma_nv=ma_nv)
    nhan_vien.tinh_luong()
    return redirect('hien_thi_nv')


def hien_thi_nv(request):
    ds_nv = NhanVien.objects.all()
    return render(request, 'app/hien_thi_nv.html', {'ds_nv':ds_nv})

def tim_nv(request):
    ma_nv = request.GET.get('ma_nv', '')
    error = None
    nhan_vien = None
    
    if ma_nv:
        try:
            nhan_vien = NhanVien.objects.get(ma_nv=ma_nv)
        except NhanVien.DoesNotExist:
            error = "Không tìm thấy nhân viên với mã này."

    return render(request, 'app/tim_nv.html', {'nhan_vien': nhan_vien, 'error': error})

def them_nv(request):
    if request.method == 'POST':
        ma_nv = request.POST['ma_nv']
        ho_ten = request.POST['ho_ten']
        luong_cb = request.POST['luong_cb']
        loai_nv = request.POST['loai_nv']
        
        so_gio_lam = request.POST.get('so_gio_lam', 0)
        so_sp = request.POST.get('so_sp', 0)
        he_so_cv = request.POST.get('he_so_cv', 0)
        thuong = request.POST.get('thuong', 0)
        
        nhan_vien = NhanVien(
            ma_nv=ma_nv, 
            ho_ten=ho_ten, 
            luong_cb=luong_cb, 
            loai_nv=loai_nv, 
            so_gio_lam=so_gio_lam, 
            so_sp=so_sp, 
            he_so_cv=he_so_cv, 
            thuong=thuong
        )
        nhan_vien.save()
        
        return redirect('hien_thi_nv')
    return render(request, 'app/them_nv.html')

def xoa_nv(request, ma_nv):
    nhan_vien = get_object_or_404(NhanVien, ma_nv=ma_nv)
    nhan_vien.delete()
    return redirect('hien_thi_nv')

def cap_nhat_nv(request, ma_nv):
    nhan_vien = get_object_or_404(NhanVien, ma_nv=ma_nv)

    if request.method == 'POST':
        nhan_vien.ho_ten = request.POST['ho_ten']
        nhan_vien.luong_cb = request.POST['luong_cb']
        nhan_vien.loai_nv = request.POST['loai_nv']

        # Cập nhật các trường riêng của từng loại nhân viên nếu có giá trị
        so_gio_lam = request.POST.get('so_gio_lam')
        so_sp = request.POST.get('so_sp')
        he_so_cv = request.POST.get('he_so_cv')
        thuong = request.POST.get('thuong')

        if so_gio_lam:
            nhan_vien.so_gio_lam = so_gio_lam
        if so_sp:
            nhan_vien.so_sp = so_sp
        if he_so_cv:
            nhan_vien.he_so_cv = he_so_cv
        if thuong:
            nhan_vien.thuong = thuong

        nhan_vien.save()
        return redirect('hien_thi_nv')

    return render(request, 'app/cap_nhat.html', {'nhan_vien': nhan_vien})




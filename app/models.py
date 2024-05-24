from django.db import models

# Create your models here.
class NhanVien(models.Model):
    ma_nv = models.IntegerField()
    ho_ten = models.CharField(max_length=200)
    luong_cb =models.IntegerField()
    loai_nv = models.CharField(max_length=100, default='van_phong')
    so_gio_lam = models.FloatField(default=0)
    so_sp = models.IntegerField(default=0)
    he_so_cv = models.FloatField(default=0)
    thuong = models.FloatField(default=0)
    luong_ht = models.FloatField(null=True)
def __str__(self):
    return str([self.ma_nv, self.ho_ten])

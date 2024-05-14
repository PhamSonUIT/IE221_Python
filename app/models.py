from django.db import models

# Create your models here.
class NhanVien(models.Model):
    ma_nv = models.IntegerField()
    ho_ten = models.CharField(max_length=200)
    luong_cb =models.IntegerField()
    so_gio_lam = models.FloatField()
    so_sp = models.IntegerField()
    he_so_cv = models.FloatField()
    thuong = models.FloatField()
    luong_ht = models.FloatField()
def __str__(self):
    return str([self.ma_nv, self.ho_ten])

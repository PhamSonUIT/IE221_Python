# Generated by Django 5.0.3 on 2024-05-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_nhanvien_loai_nv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nhanvien',
            name='he_so_cv',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='so_gio_lam',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='so_sp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='thuong',
            field=models.FloatField(default=0),
        ),
    ]

# Generated by Django 4.1.3 on 2023-01-12 10:59

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_registerdoctor_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerdoctor',
            name='status',
        ),
        migrations.AddField(
            model_name='registerdoctor',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='registerdoctor',
            name='degree',
            field=models.CharField(choices=[('Pratisyen Dr.', 'Pratisyen Dr.'), ('Dr.', 'Dr.'), ('Uzm. Dr.', 'Uzm. Dr.'), ('Doc. Dr.', 'Doc. Dr.'), ('Op. Dr.', 'Op. Dr.'), ('Doc. Dr.', 'Doc. Dr.')], max_length=20, verbose_name='Degree'),
        ),
        migrations.AlterField(
            model_name='registerdoctor',
            name='department',
            field=models.CharField(choices=[('Dermatoloji', 'Dermatoloji'), ('İç Hastalıkları', 'İç Hastalıkları'), ('Beyin ve Sinir Cerrahisi', 'Beyin ve Sinir Cerrahisi'), ('Ortopedi ve Travmatoloji', 'Ortopedi ve Travmatoloji'), ('Kulak Burun Boğaz (KBB)', 'Kulak Burun Boğaz (KBB)'), ('Onkoloji', 'Onkoloji'), ('Çocuk Hastalığı ve Hastalıkları', 'Çocuk Hastalığı ve Hastalıkları'), ('Göğüs Hastalıkları', 'Göğüs Hastalıkları'), ('Üroloji', 'Üroloji'), ('Psikiyatri', 'Psikiyatri'), ('Kadın Hastalıkları ve Doğum', 'Kadın Hastalıkları ve Doğum'), ('Göz Hastalıkları', 'Göz Hastalıkları'), ('Fiziksel Tıp ve Rehabilitasyon', 'Fiziksel Tıp ve Rehabilitasyon'), ('Diş Hekimliği', 'Diş Hekimliği'), ('Enfeksiyon Hastalıkları', 'Enfeksiyon Hastalıkları'), ('Beslenme ve Diyetetik Diyetisyen', 'Beslenme ve Diyetetik Diyetisyen')], max_length=50, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='registerdoctor',
            name='gender',
            field=models.CharField(choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadın'), ('Diğer', 'Diğer')], max_length=10, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='registerdoctor',
            name='phone_number',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(message='0 ile başlayan ve en fazla 11 haneli geçerli bir telefon numarası girin', regex=re.compile('^0\\d{1,10}$'))], verbose_name='Phone Number'),
        ),
    ]

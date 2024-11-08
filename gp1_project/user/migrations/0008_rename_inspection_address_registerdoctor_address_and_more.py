# Generated by Django 4.1.3 on 2023-01-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_registerdoctor_username_alter_registerdoctor_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerdoctor',
            old_name='inspection_address',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='doctorlogin',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='doctorlogin',
            name='password',
            field=models.CharField(blank=True, max_length=200, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='registerdoctor',
            name='username',
            field=models.CharField(max_length=25, unique=True, verbose_name='Username'),
        ),
    ]

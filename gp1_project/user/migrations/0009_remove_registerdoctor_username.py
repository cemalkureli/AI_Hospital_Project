# Generated by Django 4.1.3 on 2023-01-12 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_rename_inspection_address_registerdoctor_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerdoctor',
            name='username',
        ),
    ]

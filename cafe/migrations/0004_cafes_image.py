# Generated by Django 3.2.13 on 2022-06-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_auto_20220603_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafes',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Cafe image'),
        ),
    ]

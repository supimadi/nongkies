# Generated by Django 3.2.13 on 2022-06-09 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0008_cafes_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafepromo',
            name='image',
            field=models.CharField(max_length=120, null=True, verbose_name='Link Gambar'),
        ),
        migrations.AlterField(
            model_name='cafes',
            name='image',
            field=models.CharField(max_length=120, null=True, verbose_name='Link Gambar'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='picture',
            field=models.CharField(max_length=120, null=True, verbose_name='Link Gambar'),
        ),
    ]

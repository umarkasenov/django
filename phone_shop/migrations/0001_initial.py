# Generated by Django 4.2.10 on 2024-02-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Укажите название')),
                ('description', models.TextField(verbose_name='Укажите описание')),
                ('image_1', models.ImageField(upload_to='', verbose_name='')),
                ('image2', models.ImageField(upload_to='images')),
                ('price', models.PositiveIntegerField(verbose_name='Укажите ')),
                ('discount', models.CharField(choices=[(10, '10%'), (20, '20%'), (30, '30%'), (40, '40%'), (50, '50%'), (60, '60%'), (70, '70%'), (80, '80%'), (90, '90%'), (100, '100%')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

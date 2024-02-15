# Generated by Django 4.2.10 on 2024-02-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phoneshop',
            name='gift',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Укажите подарок к покупке'),
        ),
        migrations.AlterField(
            model_name='phoneshop',
            name='description',
            field=models.TextField(verbose_name='Укажите описание телефона'),
        ),
        migrations.AlterField(
            model_name='phoneshop',
            name='discount',
            field=models.CharField(choices=[(10, '10%'), (20, '20%'), (30, '30%'), (40, '40%'), (50, '50%')], max_length=100),
        ),
        migrations.AlterField(
            model_name='phoneshop',
            name='image2',
            field=models.URLField(blank=True, null=True, verbose_name='Укажите ссылку на фото'),
        ),
        migrations.AlterField(
            model_name='phoneshop',
            name='image_1',
            field=models.ImageField(upload_to='', verbose_name='Загрузите фото'),
        ),
        migrations.AlterField(
            model_name='phoneshop',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Укажите цену'),
        ),
        migrations.AlterField(
            model_name='phoneshop',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Укажите название телефона'),
        ),
    ]

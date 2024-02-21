# Generated by Django 4.2.10 on 2024-02-18 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone_shop', '0002_phoneshop_gift_alter_phoneshop_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phoneshop',
            options={'verbose_name': 'Телефон', 'verbose_name_plural': 'Телефоны'},
        ),
        migrations.AlterField(
            model_name='phoneshop',
            name='discount',
            field=models.CharField(choices=[('10', '10%'), ('20', '20%'), ('30', '30%'), ('40', '40%'), ('50', '50%')], max_length=100),
        ),
        migrations.CreateModel(
            name='ReviewsPhones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Напишите коментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('phone_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_phones', to='phone_shop.phoneshop')),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-03 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='meal_photo',
            field=models.ImageField(default='empty', upload_to='images/'),
        ),
    ]

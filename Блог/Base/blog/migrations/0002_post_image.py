# Generated by Django 5.0.3 on 2024-03-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='Images/default.jpg', upload_to='Images/'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friender', '0008_alter_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='photo',
            field=models.ImageField(null=True, upload_to='hotels_photo/'),
        ),
    ]

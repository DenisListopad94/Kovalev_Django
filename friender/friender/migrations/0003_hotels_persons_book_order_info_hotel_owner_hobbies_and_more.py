# Generated by Django 5.0.4 on 2024-05-13 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friender', '0002_person_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='persons',
            field=models.ManyToManyField(to='friender.person'),
        ),
        migrations.CreateModel(
            name='Book_order_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=200, null=True)),
                ('book_time', models.DateTimeField(auto_now_add=True)),
                ('hotels', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='friender.hotels')),
                ('persons', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='friender.person')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('hotels', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='friender.hotels')),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('experience', models.IntegerField(null=True)),
                ('persons', models.ManyToManyField(null=True, to='friender.person')),
                ('hotel_owner', models.ManyToManyField(null=True, to='friender.hotel_owner')),
            ],
        ),
        migrations.CreateModel(
            name='HotelsComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200, null=True)),
                ('comment_time', models.DateTimeField(auto_now_add=True)),
                ('hotels', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='friender.hotels')),
                ('persons', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='friender.person')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('id_card_number', models.IntegerField(null=True)),
                ('serial', models.CharField(max_length=30, null=True)),
                ('hotel_owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='friender.hotel_owner')),
                ('persons', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='friender.person')),
            ],
        ),
    ]

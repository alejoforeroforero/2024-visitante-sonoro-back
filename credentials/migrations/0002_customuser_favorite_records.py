# Generated by Django 5.0.6 on 2024-08-07 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
        ('recordings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='favorite_records',
            field=models.ManyToManyField(related_name='favorited_by', to='recordings.record'),
        ),
    ]

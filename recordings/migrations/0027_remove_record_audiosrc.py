# Generated by Django 5.0.6 on 2024-06-29 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordings', '0026_author_slug_alter_author_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='audioSrc',
        ),
    ]

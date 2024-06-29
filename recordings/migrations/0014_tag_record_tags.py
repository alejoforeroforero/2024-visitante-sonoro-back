# Generated by Django 5.0.6 on 2024-06-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordings', '0013_alter_record_author_alter_record_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='tags',
            field=models.ManyToManyField(related_name='recordings', to='recordings.tag'),
        ),
    ]

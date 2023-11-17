# Generated by Django 4.2.7 on 2023-11-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image_path', models.CharField(max_length=255)),
                ('dataset_image_path', models.CharField(max_length=255)),
                ('percentage', models.FloatField()),
            ],
        ),
    ]

# Generated by Django 4.2.11 on 2024-05-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_category_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
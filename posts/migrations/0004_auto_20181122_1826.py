# Generated by Django 2.1.3 on 2018-11-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20181119_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, default='', upload_to=''),
        ),
    ]
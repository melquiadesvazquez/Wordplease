# Generated by Django 2.1.3 on 2018-11-19 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.CharField(max_length=150),
        ),
    ]

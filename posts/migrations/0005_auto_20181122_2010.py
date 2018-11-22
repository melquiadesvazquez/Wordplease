# Generated by Django 2.1.3 on 2018-11-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20181122_2010'),
        ('posts', '0004_auto_20181122_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='categories.Category'),
        ),
    ]

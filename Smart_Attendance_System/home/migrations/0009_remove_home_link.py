# Generated by Django 2.1.4 on 2019-01-03 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190104_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='link',
        ),
    ]
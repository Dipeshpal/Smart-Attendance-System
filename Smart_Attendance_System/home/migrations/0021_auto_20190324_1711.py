# Generated by Django 2.1.7 on 2019-03-24 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20190323_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='slug',
            field=models.SlugField(default=569),
        ),
    ]

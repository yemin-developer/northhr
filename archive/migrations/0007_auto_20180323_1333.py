# Generated by Django 2.0.2 on 2018-03-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0006_auto_20180315_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='create_date',
            field=models.DateField(auto_now=True, verbose_name='date published'),
        ),
    ]

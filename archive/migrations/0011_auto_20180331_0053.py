# Generated by Django 2.0.2 on 2018-03-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0010_auto_20180330_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='document_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='create_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]
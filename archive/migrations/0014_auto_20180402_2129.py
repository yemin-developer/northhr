# Generated by Django 2.0.2 on 2018-04-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0013_auto_20180331_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='comment',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='log',
            name='document_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='register',
            name='comment',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='document_date',
            field=models.DateField(auto_now=True),
        ),
    ]
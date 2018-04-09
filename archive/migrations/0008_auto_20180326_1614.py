# Generated by Django 2.0.2 on 2018-03-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0007_auto_20180323_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ['person', 'category']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='register',
            options={'ordering': ['person', 'category']},
        ),
        migrations.AddField(
            model_name='person',
            name='code',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AddField(
            model_name='person',
            name='unit',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]

# Generated by Django 3.2.6 on 2021-09-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='ticked',
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]

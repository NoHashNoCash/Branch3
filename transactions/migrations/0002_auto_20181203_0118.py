# Generated by Django 2.1.3 on 2018-12-03 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]

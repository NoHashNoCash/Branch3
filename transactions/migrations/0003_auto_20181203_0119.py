# Generated by Django 2.1.3 on 2018-12-03 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20181203_0118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='date',
            new_name='transdate',
        ),
    ]

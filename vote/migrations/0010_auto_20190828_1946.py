# Generated by Django 2.2.4 on 2019-08-28 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0009_auto_20190828_1929'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hints',
            new_name='Hint',
        ),
    ]
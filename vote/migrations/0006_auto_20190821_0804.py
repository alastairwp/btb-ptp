# Generated by Django 2.2.2 on 2019-08-21 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0005_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='updated_date',
            field=models.DateTimeField(blank=True),
        ),
    ]

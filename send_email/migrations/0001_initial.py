# Generated by Django 2.2.4 on 2019-10-01 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Template Name')),
                ('sender', models.CharField(max_length=255, verbose_name='Sender')),
                ('reply_to', models.CharField(max_length=255, verbose_name='Reply-To')),
                ('subject_line_template', models.CharField(max_length=255, verbose_name='Subject')),
                ('plain_text_template', models.TextField(verbose_name='Plain text template')),
                ('html_template', models.TextField(verbose_name='HTML template')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 2.2.4 on 2019-09-04 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0018_auto_20190904_0135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hint',
            old_name='hint_position',
            new_name='position',
        ),
        migrations.RenameField(
            model_name='hint',
            old_name='hint_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='question_id',
            new_name='question',
        ),
    ]

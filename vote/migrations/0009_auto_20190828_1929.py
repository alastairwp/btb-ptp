# Generated by Django 2.2.4 on 2019-08-28 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0008_vote_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Question number'),
        ),
        migrations.CreateModel(
            name='Hints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hint_text', models.CharField(max_length=255, verbose_name='Hint Text')),
                ('hint_position', models.CharField(max_length=5, verbose_name='Hint Position')),
                ('hint_question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vote.Question')),
            ],
        ),
    ]

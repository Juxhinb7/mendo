# Generated by Django 5.0.1 on 2024-04-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanagement', '0006_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='state',
            field=models.PositiveIntegerField(choices=[(1, 'Backlog'), (2, 'Active')], default=1),
        ),
        migrations.AddField(
            model_name='story',
            name='state',
            field=models.PositiveIntegerField(choices=[(1, 'Backlog'), (2, 'Active')], default=1),
        ),
        migrations.AddField(
            model_name='subtask',
            name='state',
            field=models.PositiveIntegerField(choices=[(1, 'Backlog'), (2, 'Active')], default=1),
        ),
        migrations.AddField(
            model_name='task',
            name='state',
            field=models.PositiveIntegerField(choices=[(1, 'Backlog'), (2, 'Active')], default=1),
        ),
    ]
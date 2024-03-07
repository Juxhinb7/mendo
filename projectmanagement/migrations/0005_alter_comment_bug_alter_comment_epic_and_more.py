# Generated by Django 5.0.1 on 2024-03-02 23:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanagement', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='bug',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projectmanagement.bug'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='epic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projectmanagement.epic'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projectmanagement.project'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projectmanagement.story'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='subtask',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projectmanagement.subtask'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projectmanagement.task'),
        ),
    ]

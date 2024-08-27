# Generated by Django 5.1 on 2024-08-26 20:37

import django.db.models.deletion
import django.db.models.functions.text
import my_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='category name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
                'constraints': [models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='unique_lower_name')],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='task name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='task description')),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'In progress'), (3, 'Pending'), (4, 'Blocked'), (5, 'Done')], default=1, verbose_name='task status')),
                ('deadline', models.DateTimeField(default=my_app.models.end_of_month, verbose_name='deadline date and time')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation date and time')),
                ('categories', models.ManyToManyField(blank=True, related_name='tasks', related_query_name='task', to='my_app.category', verbose_name='task categories')),
            ],
            options={
                'verbose_name': 'task',
                'db_table': '"my_app_task"',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='task name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='task description')),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'In progress'), (3, 'Pending'), (4, 'Blocked'), (5, 'Done')], default=1, verbose_name='task status')),
                ('deadline', models.DateTimeField(default=my_app.models.end_of_month, verbose_name='deadline date and time')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation date and time')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_tasks', related_query_name='sub_task', to='my_app.task', verbose_name='основная задача')),
            ],
            options={
                'verbose_name': 'subtask',
                'db_table': '"my_app_subtask"',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddConstraint(
            model_name='task',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('title'), name='my_app_task_name_lower_unique'),
        ),
        migrations.AddConstraint(
            model_name='subtask',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('title'), name='my_app_subtask_name_lower_unique'),
        ),
    ]

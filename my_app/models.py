from django.db import models
from django.db.models.functions import Lower
import calendar
from datetime import datetime
from django.utils import timezone

def end_of_month():
    today = timezone.now()
    end_of_month = calendar.monthrange(today.year, today.month)[1]
    end_of_month_date = datetime(today.year, today.month, end_of_month)
    return end_of_month_date.astimezone()

class StatusType(models.IntegerChoices):
    NEW = 1, "New"
    IN_PROGRESS = 2, "In progress"
    PENDING = 3, "Pending"
    BLOCKED = 4, "Blocked"
    DONE = 5, "Done"

class Category(models.Model):
    name = models.CharField(verbose_name='category name', max_length=100)
    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        constraints = [
            models.UniqueConstraint(Lower('name'), name='unique_lower_name')
        ]
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(verbose_name='task name', max_length=100)
    description = models.TextField(verbose_name='task description', blank=True, null=True)
    status = models.IntegerField(verbose_name='task status', 
                              choices=StatusType.choices, default=StatusType.NEW)
    deadline = models.DateTimeField(verbose_name='deadline date and time', default=end_of_month)
    created_at = models.DateTimeField(verbose_name='creation date and time', auto_now_add=True)
    categories = models.ManyToManyField(to=Category, related_name='tasks', related_query_name='task', 
                                        verbose_name='task categories', blank=True)
    class Meta:
        db_table = '"my_app_task"'
        verbose_name = 'task'
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(Lower('title'), name='%(app_label)s_%(class)s_name_lower_unique')
        ]
    def __str__(self):
        return self.title

class SubTask(models.Model):
    title = models.CharField(verbose_name='task name', max_length=100)
    description = models.TextField(verbose_name='task description', blank=True, null=True)
    status = models.IntegerField(verbose_name='task status', 
                              choices=StatusType.choices, default=StatusType.NEW)
    deadline = models.DateTimeField(verbose_name='deadline date and time', default=end_of_month)
    created_at = models.DateTimeField(verbose_name='creation date and time', auto_now_add=True)
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE, related_name='sub_tasks', 
                             related_query_name='sub_task', verbose_name='основная задача')
    class Meta:
        db_table = '"my_app_subtask"'
        verbose_name = 'subtask'
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(Lower('title'), name='%(app_label)s_%(class)s_name_lower_unique')
        ]
    def __str__(self):
        return self.title

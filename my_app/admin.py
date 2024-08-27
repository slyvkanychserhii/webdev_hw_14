from django.contrib import admin
from .models import Category, Task, SubTask

admin.site.register(Category)

@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    exclude = ['created_at']

@admin.register(SubTask)
class SubTaskModelAdmin(admin.ModelAdmin):
    exclude = ['created_at']

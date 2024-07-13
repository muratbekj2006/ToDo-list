from django.contrib import admin

from .models import*

# Register your models here.

admin.site.register(ToDoList)
admin.site.register(ToDoType)
admin.site.register(TodoItem)
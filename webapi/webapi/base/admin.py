from django.contrib import admin
from .models import Board, Team, Task, Todo, Worker

# Register your models here.

class TodoInline(admin.TabularInline):
    model = Todo
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    model = Task
    inlines = (TodoInline, )

admin.site.register(Task, TaskAdmin)


class TaskInline(admin.TabularInline):
    model = Task
    extra = 0


class BoardAdmin(admin.ModelAdmin):
    model = Board
    fields = ("name", "position")
    list_display = ("name", "position")
    inlines = (TaskInline, )

admin.site.register(Board, BoardAdmin)


class TodoAdmin(admin.ModelAdmin):
    model = Todo

admin.site.register(Todo, TodoAdmin)



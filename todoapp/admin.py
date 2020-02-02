from django.contrib import admin
from todoapp.models import TodoApp

# Register your models here.
class TodoAppAdmin(admin.ModelAdmin):
    fields=['description','type']
admin.site.register(TodoApp)

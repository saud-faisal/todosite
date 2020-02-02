from django.db import models

# Create your models here.
class TodoApp(models.Model):
    description=models.CharField(max_length=50)
    type=models.CharField(max_length=50)

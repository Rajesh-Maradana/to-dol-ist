from django.db import models

# Create your models here.
class Todo(models.Model):
    add_date=models.DateField()
    text=models.TextField()
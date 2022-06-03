from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoModel(models.Model):
    work = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.work
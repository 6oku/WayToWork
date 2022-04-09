from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=255, default ='New Note', null=False)
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notepadname', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)


class List(models.Model):
    item = models.CharField(max_length=200, default='New Item')
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
            return self.item + ' | ' + str(self.completed)

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    user = models.name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.name = models.CharField(max_length=255,blank=True, null=True)
    description = models.name = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
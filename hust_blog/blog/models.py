from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100) # max_length is mandatory
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # If delete user then delete the whole post
    date_created = models.DateTimeField(auto_now_add=True)
    
    # Arrange most recent post on top
    class Meta:
        ordering = ('-date_created',)
    
    def __str__(self):
        return self.title

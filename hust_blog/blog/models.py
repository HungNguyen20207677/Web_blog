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
        
    def comment_count(self):
        return self.comment_set.all().count()
    
    def comments(self):
        return self.comment_set.all()
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content

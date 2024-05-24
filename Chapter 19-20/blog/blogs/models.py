from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """A blog model"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class BlogPost(models.Model):
    """A blog post as part of a blogo"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, default='')
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.title) > 50:
            return f"{self.title[:50]}..."
        else:
            return self.title
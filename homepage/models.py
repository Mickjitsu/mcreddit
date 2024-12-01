from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Thread(models.Model):
    title = models.CharField(max_length=200)  # Title of the thread
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # User who created the thread
    content = models.TextField() #The opening thread message/post
    category = models.ForeignKey(Category, related_name="threads", on_delete=models.CASCADE)  # Category the thread belongs to
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time the thread was created
    updated_at = models.DateTimeField(auto_now=True)  # Date and time the thread was last updated
    views = models.PositiveIntegerField(default=0)  # Number of views for the thread
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    thread = models.ForeignKey(Thread, related_name="posts", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # User who posted
    content = models.TextField()  # The content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time the post was created
    updated_at = models.DateTimeField(auto_now=True)  # Date and time the post was last updated
    edited = models.BooleanField(default=False)  # Whether the post was edited
    
    def __str__(self):
        return f"Post by {self.author.username} in {self.thread.title}"

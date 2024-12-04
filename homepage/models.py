from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Thread(models.Model):
    title = models.CharField(max_length=200)  # Title of the thread
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # User who created the thread
    content = models.TextField()  # The opening thread message/post
    category = models.ForeignKey('Category', related_name="threads", on_delete=models.CASCADE)  # Category the thread belongs to
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time the thread was created
    updated_at = models.DateTimeField(auto_now=True)  # Date and time the thread was last updated
    views = models.PositiveIntegerField(default=0)  # Number of views for the thread
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='threads/', blank=True, null=True)  # Optional image field
    is_approved = models.BooleanField(default=False)  # Flag to check if the thread is approved by admin

    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

    def get_upvotes_count(self):
        return Vote.objects.filter(thread=self, vote_type='upvote').count()

    def get_downvotes_count(self):
        return Vote.objects.filter(thread=self, vote_type='downvote').count()

    def get_excerpt(self):
        return Truncator(self.content).chars(200)  # Dynamic excerpt of the first 200 characters of content

    def save(self, *args, **kwargs):
        # Automatically create a slug from the title if slug is left empty
        if not self.slug:
            self.slug = slugify(self.title)
        super(Thread, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    thread = models.ForeignKey(Thread, related_name="posts", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # User who posted
    content = models.TextField()  # The content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time the post was created
    updated_at = models.DateTimeField(auto_now=True)  # Date and time the post was last updated
    edited = models.BooleanField(default=False)  # Whether the post was edited

    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    
    def get_upvotes_count(self):
        return Vote.objects.filter(comment=self, vote_type='upvote').count()

    def get_downvotes_count(self):
        return Vote.objects.filter(comment=self, vote_type='downvote').count()
        
    def __str__(self):
        return f"Post by {self.author.username} in {self.thread.title}"

class Vote(models.Model):
    VOTE_CHOICES = [
        ('upvote', 'Upvote'),
        ('downvote', 'Downvote')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who voted
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.CASCADE)  # Associated thread
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)  # Associated comment
    vote_type = models.CharField(max_length=8, choices=VOTE_CHOICES)  # Type of vote
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures that a user can only vote once per thread or comment
        unique_together = ('user', 'thread', 'comment')

    def __str__(self):
        return f"{self.user.username} voted {self.vote_type} on {self.thread.title if self.thread else self.comment.id}"
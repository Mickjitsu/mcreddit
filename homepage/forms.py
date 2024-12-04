from django import forms
from .models import Thread, Category, Comment

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content', 'image'] 

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
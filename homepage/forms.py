from django import forms
from .models import Thread, Category

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content', 'image'] 
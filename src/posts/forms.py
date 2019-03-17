from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs = {
        'class': 'form-control',
        'placeholder': 'Type Your Comment Here',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('content',)
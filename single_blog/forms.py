from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    """Form definition for Comment."""

    class Meta:
        """Meta definition for Commentform."""

        model = Comment
        fields = ('body',)

class DeleteConfirmationForm(forms.Form):
    confirmation = forms.BooleanField()
    slug = forms.CharField()

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','PostImg'] 
    
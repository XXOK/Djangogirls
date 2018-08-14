from django import forms
from blog.models import Post, Comment, Place
from .widgets import LocationWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
            'photo': forms.FileInput(attrs={'style': 'font-size: 11'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3, 'cols': 10}),
        }


class MapForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
        widgets = {
            'location': LocationWidget,
        }
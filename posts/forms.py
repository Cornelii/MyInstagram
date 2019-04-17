from django import forms
from .models import Post, Comment


# PostModelForm to manipulate Post model

class PostModelForm(forms.ModelForm):
    # 1. What input fields this form have.
    content = forms.CharField(label="content", widget=forms.Textarea(attrs={
        "placeholder":"What's Up~!"
    }))
    
    
    # 2. To set properties of corresponding inputs.
    class Meta:
        model = Post
        fields = ["content", 'image']


class CommentModelForm(forms.ModelForm):
    content = forms.CharField(label='', widget = forms.TextInput(
        attrs={
            'placeholder':"댓글 달기..."
            
        }))
    
    class Meta:
        model = Comment
        fields = ['content']

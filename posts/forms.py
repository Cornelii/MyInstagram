from django import forms
from .models import Post


# PostModelForm to manipulate Post model

class PostModelForm(forms.ModelForm):
    # 1. What input fields this form have.
    content = forms.CharField(label="content", widget=forms.Textarea(attrs={
        "placeholder":"What's Up~!"
    }))
    
    
    # 2. To set propertiesof corresponding inputs.
    class Meta:
        model = Post
        fields = ["content"]
    
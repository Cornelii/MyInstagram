from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
# from django.contrib.auth.model
from django.forms import ModelForm
from .models import Profile

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email','last_name','first_name')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'nickname',]
        

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # fields = UserCreationForm.Meta.fields
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import CustomUserChangeForm, ProfileForm, CustomUserCreationForm

from django.contrib.auth import get_user_model

from django.contrib.auth import update_session_auth_hash
from .models import Profile

from django.core.exceptions import ObjectDoesNotExist
from posts.forms import CommentModelForm

# Create your views here.

from IPython import embed

def login(request):
    
    if request.method == "GET":
        '''
        form = AuthenticationForm()
        reutnr render(request, 'accounts/login.html', {'form':form})
        '''
        return render(request, 'accounts/login.html')
    else:
        
        '''
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:list')
        '''
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'posts:list')
        else:
            return redirect('accounts:login')
    

def logout(request):
    auth_logout(request)
    return redirect('posts:list')


def signup(request):
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  ## 동시에 1:1 레코드 생기도록.
            auth_login(request, user)
            return redirect('posts:list')
    else:
        form = CustomUserCreationForm()
        
    return render(request,'accounts/signup.html',{'form':form})
        

def people(request, username):
    
    people = get_object_or_404(get_user_model(), username=username)
    profile = get_object_or_404(Profile, user=people)
    # 1. settings.AUTH_USER_MODEL (django.conf)
    # 2. get_user_model() (django.contrib.auth)  ## recommended~!
    # 사용 지양할 것. ### 3. User (django.contrib.auth.models.User) ### 안쓰는게 좋음.
    comment_form = CommentModelForm()
    return render(request, 'accounts/people.html', {
        'people':people,
        'comment_form':comment_form,
        'profile':profile
    })


# 회원 정보 변경(편집 & 반영)
def update(request):
    if request.method == "POST":
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_change_form.is_valid() and profile_form.is_valid():
            user = user_change_form.save()
            profile_form.save()
            #user = user_change_form.get_user()
            
            return redirect('people', user.username)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        profile, created = Profile.objects.get_or_create(user=request.user)
        
        profile_form = ProfileForm(instance=request.user.profile)
        
        # if hasattr(request.user, 'profile'):
        #     profile_form = ProfileForm(instance=request.user.profile)
        # else:
        #     profile_form = Profile.objects.create(user=request.user)
        
        return render(request, 'accounts/update.html', {
            'user_change_form':user_change_form,
            'profile_form':profile_form
        })


def delete(request):
    if request.method == "POST":
        request.user.delete()
        return redirect('posts:list')

    return render(request, 'accounts/delete.html')
    
    
def password(request):
    if request.method == "POST":
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            return redirect('people', request.user.username)
    else:
        password_change_form = PasswordChangeForm(request.user)
        return render(request, 'accounts/password.html',
        {
            'password_change_form':password_change_form
            
        })


def follow(request, user_id):
    followed = get_object_or_404(get_user_model(), pk=user_id) # one who is followed
    
    # 만약 현재 유저가 해당 유저를 이미 팔로우 하고 있었으면, 
    if followed in request.user.followings.all():
    #   -> 팔로우를 취소
        request.user.followings.remove(followed)
    else: # 아니면,
    #   -> 팔로우
        request.user.followings.add(followed)
        
    return redirect('people', followed.username)
    

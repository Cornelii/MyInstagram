from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import get_user_model

# Create your views here.


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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:list')
    else:
        form = UserCreationForm()
        
    return render(request,'accounts/signup.html',{'form':form})
        

def people(request, username):
    
    people = get_object_or_404(get_user_model(), username=username)
    # 1. settings.AUTH_USER_MODEL (django.conf)
    # 2. get_user_model() (django.contrib.auth)  ## recommended~!
    # 사용 지양할 것. ### 3. User (django.contrib.auth.models.User) ### 안쓰는게 좋음.
    return render(request, 'accounts/people.html', {'people':people})


from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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
        
    
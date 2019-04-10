from django.shortcuts import render, redirect
from .forms import PostModelForm
from .models import Post
# Create your views here.

def create(request):
    if request.method == "POST":
        # post를 DB에 적용.
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
        else:
            # error handling
            pass
    else:
        form = PostModelForm()
        return render(request,'posts/create.html',{
            "form":form
        })

def list(request):
    # Show all the posts.
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'posts/list.html',context)
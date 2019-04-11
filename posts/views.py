from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import PostModelForm
from .models import Post
# Create your views here.


def create(request):
    if request.method == "POST":
        # post를 DB에 적용.
        form = PostModelForm(request.POST, request.FILES)
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
    
@require_POST
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if post.user != request.user:
        return redirect('posts:list')
    post.delete()
    return redirect('posts:list')
        
def update(request, post_id):
    post = Post.objects.get(id=post_id)
    
    if post.user != request.user:
        return redirect('posts:list')
    
    
    if request.method == "POST":
        
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
        else:
            # error handling
            pass
    else:
        
        form = PostModelForm(instance=post)
        return render(request, 'posts/create.html', {
            'form':form
        })



from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .forms import PostModelForm, CommentModelForm
from .models import Post, Comment
# Create your views here.


def create(request):
    if request.method == "POST":
        # post를 DB에 적용.
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
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
        'posts':posts,
        'comment_form':CommentModelForm()
    }
    return render(request,'posts/list.html', context)


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


@login_required
def like(request, post_id):
    # 1. retrieve the post
    post = get_object_or_404(Post, id=post_id)
    
    #post.like_users.add(request.User)
    # 2. If user already like this post. Undo (Remove Like)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
    # 3. If user did not like this post yet. Like
        post.like_users.add(request.user)
    
    return redirect('posts:list')
    
    
@login_required
@require_POST
def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentModelForm(request.POST)
    if form.is_valid():
        com = form.save(commit=False)
        com.post = post
        com.user = request.user
        form.save()
        return redirect('posts:list')


@login_required
def comment_delete(request, post_id, comment_id):
    com = get_object_or_404(Comment, id=comment_id)
    post = get_object_or_404(Post, id=post_id)
    if request.user == com.user or request.user == post.user:
        com.delete()
    return redirect('posts:list')
    
    
from django.shortcuts import render, redirect
from django.http import JsonResponse

# Import models and forms
from .models import BlogPost
from .forms import BlogPostForm


def blog_index(request):
    return render(request, 'blog/blog.html')

def blog_post(request):
    posts = BlogPost.objects.all()
    content = {"posts": posts}
    return render(request, 'blog/posts.html', content)

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts') 
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})
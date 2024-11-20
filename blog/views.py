from django.shortcuts import render
from django.http import HttpResponse

# Import model Blog
from .models import Blog

def blog_index(request):
    return render(request, 'blog/index.html')
    

def blog_post(request):
    posts = Blog.objects.all()
    content = {"posts": posts}
    return render(request, 'blog/posts.html', content)
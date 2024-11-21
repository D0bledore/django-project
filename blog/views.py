from django.shortcuts import render
from django.http import HttpResponse

# Import model Blog
from .models import BlogPost

def blog_index(request):
    return render(request, 'blog/index.html')
    

def blog_post(request):
    posts = BlogPost.objects.all()
    content = {"posts": posts}
    return render(request, 'blog/posts.html', content)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Automatically set the author to the current logged-in user
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
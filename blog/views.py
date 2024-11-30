from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('user_posts', user_id=request.user.id)
            except Exception as e:
                print(f"Error saving post: {e}")  # Log the error
                form.add_error(None, f"Error saving post: {e}")
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})



def post_detail(request, post_id):
    try:
        post = BlogPost.objects.get(pk=post_id)
        return render(request, 'blog/post_detail.html', {'post': post})
    except BlogPost.DoesNotExist:
        messages.error(request, "The requested blog post does not exist.")
        return redirect('posts')  


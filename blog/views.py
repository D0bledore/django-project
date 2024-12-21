from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Import models and forms
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm
from accounts.models import CustomUser


# View to render the blog index page
def blog_index(request):
    return render(request, 'blog/blog.html')


# View to display all blog posts
def blog_post(request):
    posts = BlogPost.objects.all()
    content = {"posts": posts}
    return render(request, 'blog/posts.html', content)


# View to create a new blog post (requires login)
@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, 'Your post has been'
                                          ' created successfully!')
                return redirect('user_posts', user_id=request.user.id)
            except Exception as e:
                print(f"Error saving post: {e}")  # Log the error
                form.add_error(None, f"Error saving post: {e}")
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})


# View to display a specific blog post and its comments
def post_detail(request, post_id):
    try:
        post = BlogPost.objects.get(pk=post_id)
        comments = post.comments.filter(active=True)
        new_comment = None

        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.blog_post = post
                new_comment.author = request.user
                new_comment.save()
                messages.success(request, 'Your comment has been'
                                          ' added successfully!')
                return redirect('post_detail', post_id=post.id)
        else:
            comment_form = CommentForm()

        return render(request, 'blog/post_detail.html',
                      {'post': post,
                       'comments': comments,
                       'new_comment': new_comment,
                       'comment_form': comment_form})
    except BlogPost.DoesNotExist:
        messages.error(request, "The requested blog post does not exist.")
        return redirect('posts')


# View to edit an existing blog post (requires login)
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if post.author != request.user:
        messages.error(request, 'You are not authorized to edit this post.')
        return redirect('post_detail', post_id=post.id)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your post has been updated '
                                          'successfully!')
                return redirect('post_detail', post_id=post.id)
            except Exception as e:
                messages.error(request,
                               f'There was an error uploading your image: {e}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form})


# View to delete a blog post (requires login)
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'The post has been deleted successfully!')
        return redirect('user_posts', user_id=request.user.id)
    return render(request, 'blog/confirm_delete.html', {'post': post})


# View to display all posts by a specific user (requires login)
@login_required
def view_posts(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    posts = BlogPost.objects.filter(author=user)
    return render(request, 'blog/user_posts.html', {'posts': posts,
                                                    'profile_user': user})

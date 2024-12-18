from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
CustomUser = get_user_model()

# Import models and forms 
from blog.models import BlogPost
from blog.forms import BlogPostForm 
from .forms import ProfileForm, CustomUserCreationForm
from .models import Profile

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('profile', user_id=self.request.user.id)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def custom_logout(request):
    if request.method == 'POST':
        referer = request.META.get('HTTP_REFERER', '')
        logout(request)
        if 'profile' in referer:
            return render(request, 'accounts/logout.html')  
        return redirect('index') 
    return redirect('index') 


@login_required
def profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    profile, created = Profile.objects.get_or_create(user=user)
    posts = BlogPost.objects.filter(author=user)
    return render(request, 'accounts/profile.html', {'posts': posts, 'profile': profile})
    

@login_required
def view_posts(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    posts = BlogPost.objects.filter(author=user)
    return render(request, 'blog/user_posts.html', {'posts': posts, 'profile_user': user})


@login_required
def manage_posts(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/manage_posts.html', {'posts': posts})


@login_required
def publish_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    post.is_published = True
    post.save()
    return redirect('user_posts')

@login_required
def edit_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    profile = get_object_or_404(Profile, user=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id=user.id)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form, 'profile': profile})

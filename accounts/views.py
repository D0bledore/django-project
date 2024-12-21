from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from blog.models import BlogPost
from .forms import ProfileForm, CustomUserCreationForm
from .forms import CustomAuthenticationForm
from .models import Profile

# Get the custom user model
CustomUser = get_user_model()


# Custom login view using a custom authentication form
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('profile', user_id=self.request.user.id)


# User registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,
                             'Registration successful!'
                             ' Welcome,'
                             '{}!'.format(user.username))
            return redirect('create_post')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


# User login view
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


# User logout view
def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('index')
    return redirect('index')


# User profile view
@login_required
def profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    profile, created = Profile.objects.get_or_create(user=user)
    posts = BlogPost.objects.filter(author=user)
    return render(request, 'accounts/profile.html',
                  {'posts': posts, 'profile': profile})


# Edit user profile view
@login_required
def edit_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ProfileForm(
            request.POST, request.FILES, instance=profile, user=user)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your profile has been updated successfully!')
            print("Uploaded files:", request.FILES)
            print("Profile picture URL:", profile.profile_pic.url)
            return redirect('profile', user_id=user.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileForm(instance=profile, user=user)

    return render(request, 'accounts/edit_profile.html', {'form': form})


# Confirm delete user profile view
@login_required
def confirm_delete(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'accounts/confirm_delete.html', {'user': user})


# Delete user profile view
@login_required
def delete_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request,
                         'Your account has been deleted successfully.')
        return redirect('index')

    return render(request, 'accounts/confirm_delete.html', {'user': user})


# Change user password view
@login_required
def change_password(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,
                             'Your password has been updated successfully!')
            return redirect('profile', user_id=user.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(user)
    return render(request, 'accounts/change_password.html', {'form': form})

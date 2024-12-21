from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import CustomUser, Profile


# Form for creating a new user with custom fields
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}),
        help_text=(
            "Your password must contain at least 8 characters, "
            "including letters and numbers."
        )
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}
        ),
        help_text="Enter the same password as before, for verification."
    )
    gender = forms.ChoiceField(
        choices=CustomUser.Gender.choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ("email", "username", "password1", "password2", "gender")

    # Validate that the email is unique
    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already"
                                        "exists.")
        return email

    # Save the user with the cleaned data
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"].lower()
        user.username = self.cleaned_data["username"]
        user.gender = self.cleaned_data["gender"]
        if commit:
            user.save()
        return user


# Form for updating user information
class CustomUserChangeForm(forms.ModelForm):
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    username = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    gender = forms.ChoiceField(
        choices=CustomUser.Gender.choices,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender')

    # Validate that the email is unique
    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already "
                                        "exists.")
        return email


# Form for updating user profile information
class ProfileForm(forms.ModelForm):
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    username = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    gender = forms.ChoiceField(
        choices=CustomUser.Gender.choices,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Bio'})
    )
    profile_pic = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']

    # Initialize the form with user data
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email
            self.fields['username'].initial = user.username
            self.fields['gender'].initial = user.gender

    # Validate that the email is unique
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower()
            if CustomUser.objects.filter(
                    email__iexact=email).exclude(
                        id=self.instance.user.id).exists():
                raise forms.ValidationError("A user with that email already "
                                            "exists.")
        return email

    # Validate that the username is unique
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            username = username.lower()
            if CustomUser.objects.filter(username__iexact=username).exclude(
                    id=self.instance.user.id).exists():
                raise forms.ValidationError("A user with that username already"
                                            " exists.")
        return username

    # Save the profile and update the user information
    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        user = profile.user
        if user:
            if self.cleaned_data['email']:
                user.email = self.cleaned_data['email'].lower()
            if self.cleaned_data['username']:
                user.username = self.cleaned_data['username'].lower()
            if self.cleaned_data['gender']:
                user.gender = self.cleaned_data['gender']
            if commit:
                user.save()
                profile.save()
        return profile


# Form for authenticating users with email and password
class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Invalid email or password. Please try again.'}

    username = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))

    def clean(self):
        # Get username (email) and password from the form
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            # Authenticate the user
            self.user_cache = authenticate(self.request, username=username.lower(), password=password)
            if self.user_cache is None:
                # Raise a validation error if authentication fails
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
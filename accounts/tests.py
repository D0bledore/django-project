from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import ProfileForm, CustomAuthenticationForm
from .models import Profile

CustomUser = get_user_model()

class ProfileFormTest(TestCase):
    # Setup initial data for the tests
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='password123')
        Profile.objects.create(user=self.user)
        self.profile_data = {
            'email': 'newemail@example.com',
            'username': 'newusername',
            'gender': 'M'
        }

    # Test if the profile form is valid with correct data
    def test_profile_form_valid(self):
        form = ProfileForm(data=self.profile_data, instance=self.user.profile)
        self.assertTrue(form.is_valid())

    # Test if the profile form is invalid when the username already exists
    def test_profile_form_invalid_existing_username(self):
        CustomUser.objects.create_user(username='newusername', email='another@example.com', password='password123')
        form = ProfileForm(data=self.profile_data, instance=self.user.profile)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    # Test if the profile form saves the data correctly
    def test_profile_form_save(self):
        form = ProfileForm(data=self.profile_data, instance=self.user.profile)
        self.assertTrue(form.is_valid())
        profile = form.save()
        self.assertEqual(profile.user.email, 'newemail@example.com')
        self.assertEqual(profile.user.username, 'newusername')
        self.assertEqual(profile.user.gender, 'M')


class CustomAuthenticationFormTest(TestCase):
    # Setup initial data for the tests
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='password123')
        self.auth_data = {
            'username': 'testuser@example.com',
            'password': 'password123'
        }

    # Test if the authentication form is valid with correct data
    def test_authentication_form_valid(self):
        form = CustomAuthenticationForm(data=self.auth_data)
        self.assertTrue(form.is_valid())

    # Test if the authentication form is invalid with incorrect password
    def test_authentication_form_invalid(self):
        invalid_data = self.auth_data.copy()
        invalid_data['password'] = 'wrongpassword'
        form = CustomAuthenticationForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)


class UserViewsTest(TestCase):
    # Setup initial data for the tests
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='password123')
        self.client.login(username='testuser@example.com', password='password123')

    # Test if the confirm delete view loads correctly
    def test_confirm_delete_view(self):
        response = self.client.get(reverse('confirm_delete', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/confirm_delete.html')

    # Test if the delete profile view deletes the user and redirects correctly
    def test_delete_profile_view(self):
        response = self.client.post(reverse('delete_account', args=[self.user.id]))
        self.assertRedirects(response, reverse('index'))
        self.assertFalse(CustomUser.objects.filter(id=self.user.id).exists())

    # Test if the change password view loads and processes the form correctly
    def test_change_password_view(self):
        response = self.client.get(reverse('change_password', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/change_password.html')

        new_password_data = {
            'old_password': 'password123',
            'new_password1': 'newpassword123',
            'new_password2': 'newpassword123'
        }
        response = self.client.post(reverse('change_password', args=[self.user.id]), new_password_data)
        self.assertRedirects(response, reverse('profile', args=[self.user.id]))
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newpassword123'))

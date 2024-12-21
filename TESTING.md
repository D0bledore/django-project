# Testing

> [!NOTE]  
> Return to the [README.md](README.md) file.

## Code Validation

### HTML

All HTML files have been validated using the [HTML W3C Validator](https://validator.w3.org).

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| accounts | change_password.html | ![screenshot](documentation/validation/change_pw.png) | No errors |
| accounts | confirm_delete.html | ![screenshot](documentation/validation/confirm_del.png) | No errors |
| accounts | edit_profile.html | ![screenshot](documentation/validation/edit_profile.png) | No errors |
| accounts | login.html | ![screenshot](documentation/validation/login.png) | No errors |
| accounts | profile.html | ![screenshot](documentation/validation/profile.png) | No errors |
| accounts | register.html | ![screenshot](documentation/validation/register.png) | No site-breaking errors |
| blog | confirm_delete.html | ![screenshot](documentation/validation/post-confirm_del.png) | No errors |
| blog | create_post.html | ![screenshot](documentation/validation/posts_create.png) | No errors |
| blog | edit_post.html | ![screenshot](documentation/validation/posts_edit.png) | No errors |
| blog | post_detail.html | ![screenshot](documentation/validation/posts_detail.png) | No errors |
| blog | posts.html | ![screenshot](documentation/validation/posts.png) | No errors |
| blog | user_posts.html | ![screenshot](documentation/validation/user_posts.png) | No errors |
| core | contact.html | ![screenshot](documentation/validation/contact.png) | No errors |
| core | index.html | ![screenshot](documentation/validation/index.png) | No errors |

#### About the Warnings

All HTML pages extend `base.html`, which contains a unique `h1` element for SEO purposes.

#### About the Errors

The error detected on the account register page is not site-breaking. It is caused by Django's automatically generated `registerForm` class. The error message states: 'The `aria-describedby` attribute must point to an element in the same document', which does not exist. For SEO purposes, this issue could be addressed, but it is not critical.

### CSS

All CSS files have been validated using the [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator).

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | about.css | ![screenshot](documentation/validation/css-posts.png) | No errors |
| static | base.css | ![screenshot](documentation/validation/css-base.png) | No errors |
| static | components.css | ![screenshot](documentation/validation/css-component.png) | No errors |
| static | contact.css | ![screenshot](documentation/validation/css-contact.png) | No errors |
| static | create_post.css | ![screenshot](documentation/validation/css-create_post.png) | No errors |
| static | index.css | ![screenshot](documentation/validation/css-index.png) | No errors |
| static | layout.css | ![screenshot](documentation/validation/css-layout.png) | No errors |
| static | posts.css | ![screenshot](documentation/validation/css-posts.png) | No errors |
| static | utilities.css | ![screenshot](documentation/validation/css-utilities.png) | No errors |

### JavaScript

All JavaScript files have been validated using the [JShint Validator](https://jshint.com).

> [!NOTE]  
> Configure JSHint using the comment: `/* jshint esversion: 11 */`

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | base.js | ![screenshot](documentation/validation/js-base.png) | No errors |
| static | create_post.js | ![screenshot](documentation/validation/js-create_post.png) | No errors |
| static | edit_profile.js | ![screenshot](documentation/validation/js-edit_profile.png) | No errors |
| static | index.js | ![screenshot](documentation/validation/js-index.png) | No errors |
| static | navbar.js | ![screenshot](documentation/validation/js-navbar.png) | No errors |

### Python

All Python files have been validated using the [PEP8 CI Python Linter](https://pep8ci.herokuapp.com).

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| accounts | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/accounts/admin.py) | ![screenshot](documentation/validation/py-acc-admin.png) | |
| accounts | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/accounts/forms.py) | ![screenshot](documentation/validation/py-acc-forms.png) | |
| accounts | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/accounts/models.py) | ![screenshot](documentation/validation/py-acc-models.png) | |
| accounts | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/accounts/urls.py) | ![screenshot](documentation/validation/py-acc-urls.png) | |
| accounts | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/accounts/views.py) | ![screenshot](documentation/validation/py-acc-views.png) | |
| blog | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/blog/admin.py) | ![screenshot](documentation/validation/py-blog-admin.png) | |
| blog | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/blog/forms.py) | ![screenshot](documentation/validation/py-blog-forms.png) | |
| blog | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/blog/models.py) | ![screenshot](documentation/validation/py-blog-models.png) | |
| blog | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/blog/urls.py) | ![screenshot](documentation/validation/py-blog-urls.png) | |
| blog | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/blog/views.py) | ![screenshot](documentation/validation/py-blog-views.png) | |
| core | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/core/urls.py) | ![screenshot](documentation/validation/py-core-urls.png) | |
| core | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/core/views.py) | ![screenshot](documentation/validation/py-core-views.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/manage.py) | ![screenshot](documentation/validation/py-manage.png) | |
| projectFolder | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/projectFolder/settings.py) | ![screenshot](documentation/validation/py-settings.png) | |
| projectFolder | storage_backends.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/django-project/main/projectFolder/storage_backends.py) | ![screenshot](documentation/validation/py-storage.png) | |
| projectFolder | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledorse/django-project/main/projectFolder/urls.py) | ![screenshot](documentation/validation/py-urls.png) | |

## Browser Compatibility

The deployed project has been tested on multiple browsers to ensure compatibility.

| Browser | Home | Posts | Contact | Profile | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-posts.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-profile.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-posts.png) | ![screenshot](documentation/browsers/browser-firefox-contact.png) | ![screenshot](documentation/browsers/browser-firefox-profile.png) | Works as expected |
| Brave | ![screenshot](documentation/browsers/browser-brave-home.png) | ![screenshot](documentation/browsers/browser-brave-posts.png) | ![screenshot](documentation/browsers/browser-brave-contact.png) | ![screenshot](documentation/browsers/browser-brave-profile.png) | Works as expected |

## Responsiveness

The deployed project has been tested on multiple devices to ensure responsiveness.

| Device | Home | About | Contact | Profile | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/responsive-mobile-home.png) | ![screenshot](documentation/responsiveness/responsive-mobile-posts.png) | ![screenshot](documentation/responsiveness/responsive-mobile-contact.png) | ![screenshot](documentation/responsiveness/responsive-mobile-profile.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet-home.png) | ![screenshot](documentation/responsiveness/responsive-tablet-posts.png) | ![screenshot](documentation/responsiveness/responsive-tablet-contact.png) | ![screenshot](documentation/responsiveness/responsive-tablet-profile.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/responsive-desktop-home.png) | ![screenshot](documentation/responsiveness/responsive-desktop-posts.png) | ![screenshot](documentation/responsiveness/responsive-desktop-contact.png) | ![screenshot](documentation/responsiveness/responsive-desktop-profile.png) | Works as expected |

## Lighthouse Audit

The deployed project has been tested using the Lighthouse Audit tool to identify any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings |
| Profile | ![screenshot](documentation/lighthouse/lighthouse-profile-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-profile-desktop.png) | Some minor warnings |
| Posts | ![screenshot](documentation/lighthouse/lighthouse-posts-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-posts-desktop.png) | Slow response time due to large images |

## Defensive Programming

Defensive programming was manually tested with the following user acceptance tests:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Login | | | | | |
| | The login should display an error message when incorrect credentials are used | Tested by entering a random email and password | The Website tells me that the credentials are invalid | Test concluded and passed | ![screenshot](documentation/defensive/defensive-login.png) |
| | Both fields (Email and Username) should be case-insensitive | Tested by using a known user and entering randomly capitalized letters | The website successfully logged in as the intended user | Test concluded and passed | ![screenshot](documentation/defensive/defensive-login-case.png) |
| Register | | | | | |
| | New users should not be able to register with existing user credentials (case-insensitive) | Tested by entering capitalized letters for existing user credentials | The website correctly displayed an error that the user already exists | Test concluded and passed | ![screenshot](documentation/defensive/defensive-register.png) |
| Profile | | | | | |
| | Users should not be able to access another user's profile by changing the URL | Redirects to home and displays an error, denying permission | Tested by changing the ID number in the URL | Test concluded and passed | ![screenshot](documentation/defensive/defensive-permission-profile.png) |
| Edit Post | | | | | |
| | Users who do not own a post should not be able to edit it by adding 'edit/' to the URL | Tested by adding 'edit/' to the URL | The site redirected back to the post with an error | Test concluded and passed | ![screenshot](documentation/defensive/defensive-edit.png) |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a reader, I want to read individual blog posts in full so that I can engage with the content. | ![screenshot](documentation/story/detail.png) |
| As a user, I want to leave comments on blog posts so that I can engage with the content and share my thoughts with the author and other readers. | ![screenshot](documentation/story/comment.png) |
| As a user, I want to create an account so that I can access personalized features of the application. | ![screenshot](documentation/story/create-acc.png) |
| As a user, I want to view a list of blog posts on the website so that I can easily browse through available content. | ![screenshot](documentation/story/posts-all.png) |
| As a user, I want to edit my profile information so that I can keep my personal details up to date. | ![screenshot](documentation/story/edit-profile.png) |
| As a user, I want to log in securely to access my account and personal information. | ![screenshot](documentation/story/register-securely.png) |
| As a blogger, I want to create and publish new blog posts so that I can share my content with readers. | ![screenshot](documentation/story/create-post.png) |
| As a blogger, I want to edit and update my existing blog posts so that I can make corrections or add new information. | ![screenshot](documentation/story/edit-post.png) |
| As an admin user, I want to be able to easily review and delete inappropriate or negative comments across the site, so that I can maintain a positive and constructive environment for our community. | ![screenshot](documentation/story/deactivate-comment.png) |

## Bugs

### Django Environment Variable Bug

#### Issue
During the initial stages of the Django project, unexpected errors such as Bad Request (400) and Server Error (500) occurred.

#### Resolution
Using `load_dotenv()` resolved the issue:

```python
from dotenv import load_dotenv
load_dotenv()  # This line resolved the error. 

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = os.environ.get('DJANGO_DEBUG')
```

#### Lesson Learned
Environment variables can be tricky. Using `load_dotenv()` ensures they load correctly.

### NS_BINDING_ABORTED

I initially believed that images were being uploaded to the AWS S3 bucket, but they were not successful until I added the following lines to `account/models.py`:

```python
from storages.backends.s3boto3 import S3Boto3Storage
profile_pic = models.ImageField(storage=S3Boto3Storage(), upload_to='media/profile_pics/', blank=True, null=True)
```

### Attribute Error

Logging in with a known user but randomly capitalizing letters caused a server error. The issue was due to calling `.lower()` on an invalid value (`None`). The solution was to apply the `.lower()` transformation at the authentication stage.

## Unfixed Bugs

- HTML validation warning about lacking a header `h2-h6` in a semantic `section` element. This is acceptable.

    ![screenshot](documentation/validation/post-confirm_del.png)

- HTML validation warning about `h1` not being the top-level heading. This is acceptable.

    ![screenshot](documentation/validation/post-confirm_del.png)


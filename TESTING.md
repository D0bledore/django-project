# TESTING

This document includes required testing procedures and bug reports.  

## Bugs 
 
### Django Environment Variable Bug

#### What Happened
I was just starting my Django project, and suddenly, weird errors started popping up. First, a Bad Request (400), then it got worse - a full-blown Server Error (500)!

#### The Weird Part
- I hadn't even written much code yet
- `python3 manage.py check` showed nothing wrong

#### The Magic Fix
I discovered this little trick with `load_dotenv()` that basically saved me from frustration:

```python
from dotenv import load_dotenv
load_dotenv()  # This line resolved the error. 

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = os.environ.get('DJANGO_DEBUG')
```

#### What I Learned
Environment variables can be super tricky. Sometimes, they just don't load properly, and it can make your entire project go crazy. The `load_dotenv()` function is like a secret weapon that makes sure everything loads correctly.

#### Pro Tip for Beginners
Always use `load_dotenv()` when you're working with `.env` files. Trust me, it'll save you hours of headache! 🚀


### Null Error in URL Generation

#### What Happened 
While creating a blog post, the URL http://127.0.0.1:8000/blog/posts/create/null was generated, causing a null error.

#### The Error 
- The data-register-url attribute was not correctly set in the HTML form.
- The JavaScript code was trying to use this null value, leading to the incorrect URL.

#### The Fix
Ensure that the data-register-url attribute is correctly set in the HTML form and that the JavaScript code correctly retrieves and uses this URL. 

##### Steps to Fix 
1. Ensure data-register-url Attribute is Set:

- Make sure the data-register-url attribute is correctly set in the HTML form.
```html
<form method="post" id="createPostForm" data-register-url="{% url 'register' %}" data-is-authenticated="{{ user.is_authenticated }}">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

2. Retrieve and Use registerUrl in JavaScript:

- Ensure the JavaScript code correctly retrieves and uses the registerUrl.
```javascript
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('createPostForm');
    form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
            event.preventDefault();
            showStep(currentStep);
            return;
        }

        const postData = {
            title: form.title.value,
            category: form.category.value,
            condition: form.condition.value,
            content: form.content.value,
            price: form.price.value,
            sale_handling: form.sale_handling.value,
            email: form.email ? form.email.value : null
        };

        localStorage.setItem('postData', JSON.stringify(postData));
    });

    // Redirect to registration page if user is not authenticated
    const isAuthenticated = form.getAttribute('data-is-authenticated') === 'True';
    if (!isAuthenticated) {
        const guestFormStep = document.querySelector('.form-step:nth-last-child(2)');
        if (guestFormStep) {
            const registerUrl = form.getAttribute('data-register-url');
            if (!registerUrl) {
                console.error('Register URL is not defined');
                return;
            }
            guestFormStep.querySelector('button').addEventListener('click', function () {
                if (validateStep(currentStep)) {
                    window.location.href = registerUrl;
                }
            });
        }
    }
});
```


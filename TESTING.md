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

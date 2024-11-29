release: python manage.py migrate --no-input
release: python manage.py collectstatic --no-input
web: gunicorn projectFolder.wsgi
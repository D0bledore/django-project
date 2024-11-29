release: python manage.py migrate --no-input
release: python manage.py collectstatic --upload-unhashed-files --no-input
web: gunicorn projectFolder.wsgi
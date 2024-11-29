release: python manage.py migrate --no-input
python manage.py collectstatic --noinput --upload-unhashed-files
web: gunicorn projectFolder.wsgi
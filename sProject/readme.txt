docker run -p 8000:8000 -v ${PWD}:/srv/sProject aaa

STATIC_URL = '/static/'

# static files
STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]

STATIC_ROOT = os.path.join(BASE_DIR, '.static_root')

python manage.py collectstatic
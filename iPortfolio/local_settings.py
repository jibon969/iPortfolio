import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'Jayed-Hossain-Jibon'
DEBUG = True

ALLOWED_HOSTS = ["*"]
BASE_URL = "http://127.0.0.1:8000"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


def verified_callback(user):
    user.is_active = True


EMAIL_VERIFIED_CALLBACK = verified_callback
EMAIL_FROM_ADDRESS = 'jibon.belaface@gmail.com'
EMAIL_MAIL_SUBJECT = 'Confirm your email {{ user.username }}'
EMAIL_MAIL_HTML = 'registration/mail_body.html'
EMAIL_MAIL_PLAIN = 'registration/mail_body.txt'
EMAIL_MAIL_TOKEN_LIFE = 60 * 60
EMAIL_MAIL_PAGE_TEMPLATE = 'registration/confirm_template.html'
EMAIL_PAGE_DOMAIN = 'http://127.0.0.1:8000/'  # Host
# EMAIL_MULTI_USER = True  # optional (defaults to False)


# For Django Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jibon.belaface@gmail.com'
EMAIL_HOST_PASSWORD = 'qxhjsznfuwbmptcy'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'jibon.belaface@gmail.com'
SERVER_EMAIL = 'jibon.belaface@gmail.com'

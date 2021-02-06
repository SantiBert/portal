from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['oscardelmastro.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'OSCARDELMASTRO$oscar',
        'USER': 'OSCARDELMASTRO',
        'PASSWORD': 'sunchales',
        'HOST': 'OSCARDELMASTRO.mysql.pythonanywhere-services.com',
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


LOGIN_REDIRECT_URL = 'administration'
LOGOUT_REDIRECT_URL = 'index'

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['oscardelmastro.pythonanywhere.com']

SITE_URL_DETAIL = 'http://oscardelmastro.pythonanywhere.com/blog/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'OSCARDELMASTRO$oscar',
        'USER': 'OSCARDELMASTRO',
        'PASSWORD': 'sunchales',
        'HOST': 'OSCARDELMASTRO.mysql.pythonanywhere-services.com',
    }
}

FILES_PATH = "files/images"

STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = 'administration'
LOGOUT_REDIRECT_URL = 'index'

import os
import sys
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-n-v^5zd$jw=f0jw=$s3+0r^sk%e^1htc0y_m4jm!%)!u)27(su')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    DEBUG = DEBUG,
    SECRET_KEY = SECRET_KEY,
    ALLOWED_HOSTS = ALLOWED_HOSTS,
    ROOT_URLCONF = __name__,
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

application = get_wsgi_application()

# this should be in the views.py file
def index(request):
    return HttpResponse('Hello World')

# this should be in the the urls.py file 
urlpatterns = (
    url(r'^$', index),

)
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    
    execute_from_command_line(sys.argv)
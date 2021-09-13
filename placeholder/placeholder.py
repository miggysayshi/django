import os
import sys
from django.conf import settings

# ==================== this should be in the settings.py file ====================
DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-)_k0d(2ile0n%m)t2w)72y_x1kbeg4hctnsk0h+&bqv=#4hqm0')
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

# ==================== this should be in the views.py file ====================
from django import forms
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse, HttpResponseBadRequest
from io import BytesIO
from PIL import Image

application = get_wsgi_application()

# home page view
def index(request):
    return HttpResponse('Hello World')

# form class used to make sure that we are only accepting correct variables from the url
class ImageForm(forms.Form):
    """ Form to validate requested place holder image. """
    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)

    def generate(self, image_format='PNG'):
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        image = Image.new('RGB', (width, height))
        content = BytesIO()
        image.save(content, image_format)
        content.seek(0)
        return content


# once we finally have correct data send bad or ok response
def placeholder(request, width, height):
    # TODO: rest of the view will go here
    form = ImageForm({'height': height, 'width': width})
    if form.is_valid():
        image = form.generate()
        return HttpResponse(image, content_type='image/png')
    else:
        return HttpResponseBadRequest('Invalid Image Reequest')


# ==================== this should be in the urls.py file ====================
urlpatterns = (
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name='placeholder'),
    url(r'^$', index, name='homepage'),

)
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    
    execute_from_command_line(sys.argv)
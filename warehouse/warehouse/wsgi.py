"""
WSGI config for warehouse project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse.settings')

application = get_wsgi_application()

urlpatterns = [
   #url(r'^login/$', auth_views.login, name='login'),
   #url(r'^logout/$', auth_views.logout, name='logout'),
   #path(r'signup/$', getSignup, name='signup')
   url(r'^admin/', admin.site.urls),
]

#Add Django site authentication urls (for login, logout, password management)
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]

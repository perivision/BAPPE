"""warehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

# TODO change this import rule?
from .views.views import *
from .views.view_customer import *
from .views.view_dashboard import *
from .views.view_inventory import *
from .views.view_login import *
from .views.view_members import *
from .views.view_request_items import *
from .views.view_signup import *

urlpatterns = [
  path('addInventory/', addInventory, name='addInventory'),
  path('admin/', admin.site.urls),
  path('customer/', customer, name='customer'),
  path('dashboard/', dashboard, name='dashboard'),
  path('inTransit/', inTransit, name='intransit'),
  path('logout/', logoutUser, name='logoutUser'),
  path('login/', getLogin, name='login'),
  path('request/', requestItems, name='requestItems'),
  path('showRequests/', showRequests, name='showRequests'),
  path('signup/', getSignup, name='signup'),
  path('signupSuccess/', signupSuccess, name='registration'),
  path('viewCustomers/', viewCustomers, name='viewCustomers'),
  path('viewInventory/', viewInventory, name='viewInventory'),
  path('viewMembers/', viewMembers, name='viewMembers'),
]

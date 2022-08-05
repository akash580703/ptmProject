"""ptm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Whatsapp import functions,views,localTunnel


urlpatterns = [
    path('admin/', admin.site.urls),
    path('save/', functions.main, name='main'),
    path('start/', localTunnel.server, name='server'),
    url(r'^pdf/$', views.whatsAppApi),
    url(r'^payment/$', views.payment),
    url(r'testMe/$',views.testMe),
    url(r'^pdf/([a-z and %20 and A-Z and 0-9 and -]+)$', views.whatsAppApi),
]

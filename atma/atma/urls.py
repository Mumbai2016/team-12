"""atma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from web.views import AIP,QP,Dashboard,login,index
from django.conf.urls.static import static

from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Dashboard/(?P<NGO_selected>[a-zA-z&.0-9 ]+)/$', Dashboard),
    url(r'^login/(?P<year_selected>[0-9 ]+)/$', AIP),
    url(r'^index/', index),
    url(r'^AIP/(?P<year>[0-9])/$',AIP),	
    url(r'^QP/',QP)
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

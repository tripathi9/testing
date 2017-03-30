"""kit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from check import views
from django.contrib.auth import views as auth_views
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.main),
    url(r'^base/$', views.main),
    url(r'^register/userprofile/$', views.account),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/$', auth_views.login, {'template_name': 'check/login.html'}, name='login'),
    url(r'^register/$', views.register_page),
    url(r'^logout/$', views.logout_page),
    url(r'^accounts/profile/$', views.account),
    url(r'^profile/$', views.create_profile),
    url(r'^event/$', views.event_create),
    url(r'^eventlist/$', views.event_list),
    url(r'^updateProfile/$', views.profile_update),
    url(r'^(?P<id>[0-9]+)/edit/$', views.profile_update),
    url(r'^events/(?P<id>[0-9]+)/$', views.event_update),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

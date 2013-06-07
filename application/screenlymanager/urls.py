from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'screenlymanager.views.index', name='index'),
    url(r'^clients/?$', 'screenlymanager.views.clients', name='clients'),
    url(r'^client/(?P<pk>[0-9]+)/?$', 'screenlymanager.views.client', name='client-detail'),
    url(r'^admin/', include(admin.site.urls)),
)

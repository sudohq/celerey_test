from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'celerey_test.views.home', name='home'),
    url(r'^$', 'main.views.ur'),
    #url(r'^[a-z0-9_\/.:@]+/$', 'main.views.test2'),
    url(r'^get/$', 'main.views.ur'),
    url(r'^get/([a-z0-9_\/.:@]+)/$','main.views.pars'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

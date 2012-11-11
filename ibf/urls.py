from django.conf.urls import patterns, include, url
from ibf.views import list_users

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ibf.views.home', name='home'),
    # url(r'^ibf/', include('ibf.foo.urls')),
    url('^list_users$', list_users)

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

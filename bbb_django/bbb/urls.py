from django.conf.urls.defaults import *
from bbb.views.core import (home_page, create_meeting, begin_meeting, meetings,
                            join_meeting, delete_meeting)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('^$', home_page, name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {
            'template_name': 'login.html',
        }, name='login'),
    url(r'^logoff/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name='logout'),
    url('^create/$', create_meeting, name='create'),
    url('^begin/$', begin_meeting, name='begin'),
    url('^meetings/$', meetings, name='meetings'),
    url('^meeting/(?P<meeting_id>[a-zA-Z0-9 _-]+)/join$', join_meeting,
        name='join'),
    url('^meeting/(?P<meeting_id>[a-zA-Z0-9 _-]+)/(?P<password>.*)/delete$', delete_meeting,
        name='delete'),
    url('^help.html$', 'django.views.generic.simple.redirect_to', {
            'url': 'http://www.bigbluebutton.org/content/videos' ,
        }, name='help'),
)

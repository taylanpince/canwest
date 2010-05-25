from django.conf.urls.defaults import *


urlpatterns = patterns('twitter.views',
    url(r'^$', 'landing', name='twitter_landing'),
    url(r'^auth/$', 'landing_auth', name='twitter_landing_auth'),
    url(r'^auth/begin/$', 'auth', name='twitter_auth'),
    url(r'^auth/complete/$', 'auth_complete', name='twitter_auth_complete'),
    url(r'^auth/clear/$', 'auth_clear', name='twitter_auth_clear'),
    url(r'^error/$', 'error', name='twitter_error'),
    url(r'^update/$', 'update', name='twitter_update'),
)

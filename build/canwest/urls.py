from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Admin
    (r'^admin/', include(admin.site.urls)),
    
    # Home
    url(r"^$", "shows.views.home", name="home"),
    
    # Contests
    url(r"^contests/$", "contests.views.list", name="contests_list"),
    
    # Shows
    url(r"^shows/$", "shows.views.list", name="shows_list"),
    url(r"^shows/(?P<category_slug>[-\w]+)/$", "shows.views.category", name="shows_category"),
    url(r"^shows/(?P<category_slug>[-\w]+)/channels/(?P<slug>[-\w]+)/$", "shows.views.channel", name="shows_channel"),
    url(r"^shows/(?P<category_slug>[-\w]+)/shows/(?P<slug>[-\w]+)/$", "shows.views.detail", name="shows_detail"),
    
    # Schedules
    url(r"^schedules/$", "schedules.views.list", name="schedules_list"),
    
    # Twitter
    (r'^twitter/', include('twitter.urls')),
)

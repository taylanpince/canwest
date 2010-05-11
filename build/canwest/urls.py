from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Admin
    (r'^admin/', include(admin.site.urls)),
    
    # Contests
    url(r"^contests/$", "contests.views.list", name="contests_list"),
    
    # Shows
    url(r"^shows/$", "contests.views.list", name="shows_list"),
    url(r"^shows/(?P<slug>[-\w]+)/$", "contests.views.detail", name="shows_detail"),
)

import os
import sys
import site

site.addsitedir('/home/taylan/sites/canwest/lib/python2.5/site-packages')

sys.path.append("/home/taylan/sites/canwest/src/canwest/build")
sys.path.append("/home/taylan/sites/canwest/src/canwest/build/canwest")

os.environ["DJANGO_SETTINGS_MODULE"] = "canwest.settings"

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

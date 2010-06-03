import re

from django.conf import settings
from django.utils.safestring import mark_safe

from hashlib import md5
from random import randint
from urllib import quote_plus, urlencode
from uuid import uuid4


REMOTE_ADDRESS_RE = re.compile(r"^([^.]+\.[^.]+\.[^.]+\.).*")
GOOGLE_ANALYTICS_BASE_PATH = "http://www.google-analytics.com/__utm.gif"
GOOGLE_ANALYTICS_ACCOUNT = getattr(settings, "GOOGLE_ANALYTICS_ACCOUNT", None)


def google_analytics_path(request):
    """
    Constructs the request URL for Google Analytics image tracking
    """
    visitor_ip = ""
    visitor_id = "0x"

    if request.META.get("HTTP_X_DCMGUID", None):
        visitor_id += md5(request.META.get("HTTP_X_DCMGUID") + GOOGLE_ANALYTICS_ACCOUNT).hexdigest()[:16]
    else:
        visitor_id += md5(request.META.get("HTTP_USER_AGENT", "") + str(uuid4())).hexdigest()[:16]

    if request.META.get("REMOTE_ADDR", None):
        matches = re.match('^([^.]+\.[^.]+\.[^.]+\.).*', request.META.get("REMOTE_ADDR"))

        if matches:
            visitor_ip = matches.groups()[0] + "0"

    params = {
        "utmwv": "4.4sh",
        "utmn": str(randint(0, 0x7fffffff)),
        "utmhn": request.META.get("HTTP_HOST", ""),
        "utmsr": "",
        "utme": "",
        "utmr": quote_plus(request.META.get("HTTP_REFERER", "")),
        "utmp": quote_plus(request.META.get("REQUEST_URI", "")),
        "utmac": GOOGLE_ANALYTICS_ACCOUNT,
        "utmcc": "__utma%3D999.999.999.999.999.1%3B",
        "utmvid": visitor_id,
        "utmip": visitor_ip,
    }

    return {
        "GOOGLE_ANALYTICS_PATH": mark_safe("%(url)s?%(query)s" % {
            "url": GOOGLE_ANALYTICS_BASE_PATH,
            "query": urlencode(params),
        }),
    }


def device(request):
    """
    Adds request.device to the context
    """
    DEVICE_IPHONE = False
    DEVICE_BLACKBERRY_450 = False
    DEVICE_BLACKBERRY_500 = False
    DEVICE_DESKTOP = False
    FULL_WIDTH = 480
    HALF_WIDTH = 240
    THUMB_WIDTH = 150

    if request.device.get("mobileDevice", False) and request.device.get("osOsx", False):
        DEVICE_IPHONE = True
        FULL_WIDTH = 320
        HALF_WIDTH = 160
        THUMB_WIDTH = 100
    elif (request.device.get("mobileDevice", False) and request.device.get("osRim", False) and request.device.get("displayWidth") <= 320) or "BlackBerry8530" in request.device.get("_matched", ""):
        DEVICE_BLACKBERRY_450 = True
        FULL_WIDTH = 308
        HALF_WIDTH = 154
        THUMB_WIDTH = 100
    elif request.device.get("mobileDevice", False) and request.device.get("osRim", False):
        DEVICE_BLACKBERRY_500 = True
        FULL_WIDTH = 478
        HALF_WIDTH = 239
    else:
        DEVICE_DESKTOP = True

    return {
        "DEVICE_IPHONE": DEVICE_IPHONE,
        "DEVICE_BLACKBERRY_450": DEVICE_BLACKBERRY_450,
        "DEVICE_BLACKBERRY_500": DEVICE_BLACKBERRY_500,
        "DEVICE_DESKTOP": DEVICE_DESKTOP,
        "FULL_WIDTH": FULL_WIDTH,
        "HALF_WIDTH": HALF_WIDTH,
        "THUMB_WIDTH": THUMB_WIDTH,
    }

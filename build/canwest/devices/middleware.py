from django.conf import settings

from devices.deviceatlas import DeviceAtlas


DEVICE_ATLAS_PATH = getattr(settings, "DEVICE_ATLAS_PATH", None)
DEVICE_ATLAS = DeviceAtlas(DEVICE_ATLAS_PATH)


class DeviceDetectMiddleware(object):
    def process_request(self, request):
        """
        Adds device information to every request
        """
        request.device = DEVICE_ATLAS.device(request.META["HTTP_USER_AGENT"])



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
    elif request.device.get("mobileDevice", False) and request.device.get("osRim", False) and request.device.get("displayWidth") <= 320:
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

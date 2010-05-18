

def device(request):
    """
    Adds request.device to the context
    """
    return {
        "DEVICE": request.device,
    }

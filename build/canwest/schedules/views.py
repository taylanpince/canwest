from django.shortcuts import render_to_response
from django.template import RequestContext

from admob.decorators import admob_analytics
from schedules.models import ScheduledItem, DAY_CHOICES


@admob_analytics
def list(request):
    """
    A list of all scheduled items, grouped by day
    """
    days = dict(DAY_CHOICES).keys()
    scheduled_items = ScheduledItem.objects.all().order_by("day")
    sorted_items = sorted(scheduled_items, key=lambda item: days.index(item.day))

    return render_to_response("schedules/list.html", {
        "scheduled_items": sorted_items,
        "USE_GLOBAL_TEMPLATE": True,
    }, context_instance=RequestContext(request))

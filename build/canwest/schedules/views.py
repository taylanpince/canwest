from django.shortcuts import render_to_response
from django.template import RequestContext

from admob.decorators import admob_analytics
from schedules.models import ScheduledItem


@admob_analytics
def list(request):
    """
    A list of all scheduled items, grouped by day
    """
    scheduled_items = ScheduledItem.objects.all().order_by("day")

    return render_to_response("schedules/list.html", {
        "scheduled_items": scheduled_items,
        "USE_GLOBAL_TEMPLATE": True,
    }, context_instance=RequestContext(request))

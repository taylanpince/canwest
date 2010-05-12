from django.shortcuts import render_to_response
from django.template import RequestContext

from schedules.models import ScheduledItem


def list(request):
    """
    A list of all scheduled items, grouped by day
    """
    scheduled_items = ScheduledItem.objects.all()

    return render_to_response("schedules/list.html", {
        "scheduled_items": scheduled_items,
    }, context_instance=RequestContext(request))

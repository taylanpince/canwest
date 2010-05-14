from django.shortcuts import render_to_response
from django.template import RequestContext

from admob.decorators import analytics
from contests.models import Contest


@analytics
def list(request):
    """
    A list of all contests
    """
    contests = Contest.objects.all()

    return render_to_response("contests/list.html", {
        "contests": contests,
    }, context_instance=RequestContext(request))

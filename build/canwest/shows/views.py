from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from shows.models import Show


def list(request):
    """
    A list of all shows
    """
    shows = Show.objects.all()

    return render_to_response("shows/list.html", {
        "shows": shows,
    }, context_instance=RequestContext(request))


def detail(request, slug):
    """
    A list of all shows
    """
    show = get_object_or_404(Show, slug=slug)

    return render_to_response("shows/detail.html", {
        "show": show,
    }, context_instance=RequestContext(request))

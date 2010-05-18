from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from admob.decorators import admob_analytics
from shows.models import Show, Channel, ShowCategory


@admob_analytics
def list(request):
    """
    A list of all show categories
    """
    categories = ShowCategory.objects.all()

    return render_to_response("shows/list.html", {
        "categories": categories,
    }, context_instance=RequestContext(request))


@admob_analytics
def category(request, category_slug):
    """
    A list of all shows in a given category
    """
    category = get_object_or_404(ShowCategory, slug=category_slug)

    return render_to_response("shows/category.html", {
        "category": category,
        "USE_GLOBAL_TEMPLATE": category.global_template,
    }, context_instance=RequestContext(request))


@admob_analytics
def channel(request, category_slug, slug):
    """
    Renders a list of shows tied to this channel
    """
    channel = get_object_or_404(Channel, slug=slug)

    return render_to_response("shows/channel.html", {
        "channel": channel,
        "USE_GLOBAL_TEMPLATE": channel.category.global_template,
    }, context_instance=RequestContext(request))


@admob_analytics
def detail(request, category_slug, slug):
    """
    Show details
    """
    show = get_object_or_404(Show, slug=slug)

    return render_to_response("shows/detail.html", {
        "show": show,
        "USE_GLOBAL_TEMPLATE": show.category.global_template,
    }, context_instance=RequestContext(request))


@admob_analytics
def home(request):
    """
    Renders the home page
    """
    return render_to_response("home.html", {
        
    }, context_instance=RequestContext(request))

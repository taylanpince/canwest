from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from shows.models import Show, ShowCategory


def list(request):
    """
    A list of all show categories
    """
    categories = ShowCategory.objects.all()

    return render_to_response("shows/list.html", {
        "categories": categories,
    }, context_instance=RequestContext(request))


def category(request, category_slug):
    """
    A list of all shows in a given category
    """
    category = get_object_or_404(ShowCategory, slug=category_slug)

    return render_to_response("shows/category.html", {
        "category": category,
        "USE_GLOBAL_TEMPLATE": category.global_template,
    }, context_instance=RequestContext(request))


def detail(request, category_slug, slug):
    """
    Show details
    """
    show = get_object_or_404(Show, slug=slug)

    return render_to_response("shows/detail.html", {
        "show": show,
        "USE_GLOBAL_TEMPLATE": show.category.global_template,
    }, context_instance=RequestContext(request))

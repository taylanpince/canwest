import datetime
import httplib
import oauth
import time

from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

from admob.decorators import admob_analytics
from twitter.forms import StatusUpdateForm
from twitter.utils import *


CONSUMER = oauth.OAuthConsumer(CONSUMER_KEY, CONSUMER_SECRET)
CONNECTION = httplib.HTTPSConnection(SERVER)
SEARCH_CONNECTION = httplib.HTTPConnection(SEARCH_SERVER)
SEARCH_RESULTS_KEY = "twitter_search_results"


@admob_analytics
def landing(request):
    """
    Twitter landing page with status update form and search results
    """
    if request.session.has_key("access_token"):
        form = StatusUpdateForm()
    else:
        form = None

    results = cache.get(SEARCH_RESULTS_KEY)

    if not results:
        json = get_search_results(SEARCH_CONNECTION, "#Canwest")
        results = simplejson.loads(json)

        cache.set(SEARCH_RESULTS_KEY, results, 30 * 60)

    return render_to_response("twitter/landing.html", {
        "form": form,
        "results": results.get("results", None),
        "sent": request.GET.has_key("sent"),
    }, context_instance=RequestContext(request))


def update(request):
    """
    Update user's Twitter status
    """
    form = StatusUpdateForm(request.POST)

    if form.is_valid():
        access_token = request.session.get("access_token", None)

        if not access_token:
            return HttpResponseRedirect(reverse("twitter_error"))

        token = oauth.OAuthToken.from_string(access_token)   
        response = update_status(CONSUMER, CONNECTION, token, form.cleaned_data.get("status"))

        if response:
            cache.delete(SEARCH_RESULTS_KEY)

            return "%s?sent=True" % HttpResponseRedirect(reverse("twitter_landing"))
        else:
            return HttpResponseRedirect(reverse("twitter_error"))

    return render_to_response("twitter/update.html", {
        "form": form,
    }, context_instance=RequestContext(request))


def auth_clear(request):
    """
    Remove authentication
    """
    response = HttpResponseRedirect(reverse("twitter_landing"))
    request.session.clear()

    return response


def auth(request):
    """
    Authenticate the user with Twitter
    """
    token = get_unauthorised_request_token(CONSUMER, CONNECTION)
    auth_url = get_authorisation_url(CONSUMER, token)
    response = HttpResponseRedirect(auth_url)

    request.session["unauthed_token"] = token.to_string()

    return response


def auth_complete(request):
    """
    Validate and save Twitter auth token
    """
    unauthed_token = request.session.get("unauthed_token", None)

    if not unauthed_token:
        return HttpResponseRedirect(reverse("twitter_error"))

    token = oauth.OAuthToken.from_string(unauthed_token)   

    if token.key != request.GET.get("oauth_token", "no-token"):
        return HttpResponseRedirect(reverse("twitter_landing"))

    access_token = exchange_request_token_for_access_token(CONSUMER, CONNECTION, token)
    response = HttpResponseRedirect(reverse("twitter_landing"))

    request.session["access_token"] = access_token.to_string()

    return response


def error(request):
    """
    A simple error page
    """
    return render_to_response("twitter/error.html", {
    
    }, context_instance=RequestContext(request))

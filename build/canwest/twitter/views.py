import datetime
import httplib
import oauth
import time

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

from twitter.forms import StatusUpdateForm
from twitter.utils import *


CONSUMER = oauth.OAuthConsumer(CONSUMER_KEY, CONSUMER_SECRET)
CONNECTION = httplib.HTTPSConnection(SERVER)


def landing(request):
    """
    Twitter landing page with status update form and search results
    """
    return render_to_response("twitter/landing.html", {
        "form": StatusUpdateForm(),
        "has_auth": request.session.has_key("access_token"),
    }, context_instance=RequestContext(request))


def update_status(request):
    """
    Update user's Twitter status
    """
    form = StatusUpdateForm(request.POST)

    if form.is_valid():
        access_token = request.session.get("access_token", None)

        if not access_token:
            return HttpResponseRedirect(reverse("twitter_error"))

        token = oauth.OAuthToken.from_string(access_token)   
        response = update_status(CONSUMER, CONNECTION, access_token, form.cleaned_data.get("status"))
        print response
        if response:
            return HttpResponseRedirect(reverse("twitter_landing"))

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
        return HttpResponseRedirect(reverse("twitter_error"))

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

from django import forms
from django.utils.translation import ugettext_lazy as _


class StatusUpdateForm(forms.Form):
    """
    A simple form for updating user's Twitter status
    """
    status = forms.CharField(label=_("Status"), initial="#Canwest", max_length=140, widget=forms.Textarea)

from django import forms
from django.utils.translation import ugettext_lazy as _


class StatusUpdateForm(forms.Form):
    """
    A simple form for updating user's Twitter status
    """
    status = forms.CharField(label=_("Status"), initial="#canwestca", widget=forms.Textarea)

    def clean_status(self):
        data = self.cleaned_data.get("status", None)

        if not data or data == "#Canwest" or data == "":
            raise forms.ValidationError(_("Please enter your tweet below"))
        elif len(data) > 140:
            raise forms.ValidationError(_("Your tweet is %d characters long. Max 140 characters." % len(data)))

        return data

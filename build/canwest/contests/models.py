from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contest(models.Model):
    """
    A simple contest with title, copy and sponsors
    """
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255)
    description = models.TextField(_("Description"), blank=True)

    class Meta:
        verbose_name = _("Contest")
        verbose_name_plural = _("Contests")

    def __unicode__(self):
        return self.title


class Sponsor(models.Model):
    """
    A sponsor, tied to a contest
    """
    name = models.CharField(_("Name"), max_length=255)
    url = models.URLField(_("URL"), blank=True, verify_exists=False)
    logo = models.ImageField(_("Logo"), upload_to="files/sponsors")
    contest = models.ForeignKey(Contest, verbose_name=_("Contest"), related_name="sponsors")

    class Meta:
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsors")

    def __unicode__(self):
        return self.name

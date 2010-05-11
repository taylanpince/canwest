from django.db import models
from django.utils.translation import ugettext_lazy as _


class Show(models.Model):
    """
    A TV show with title, description and photo
    """
    title = models.CharField(_("Title"), max_length=255)
    blurb = models.TextField(_("Blurb"), blank=True)
    description = models.TextField(_("Description"), blank=True)
    photo = models.ImageField(_("Photo"), upload_to="files/shows")

    class Meta:
        verbose_name = _("Show")
        verbose_name_plural = _("Shows")

    def __unicode__(self):
        return self.title

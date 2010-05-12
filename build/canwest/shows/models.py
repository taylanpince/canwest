from django.db import models
from django.utils.translation import ugettext_lazy as _


class ShowCategory(models.Model):
    """
    A show category
    """
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255)
    global_template = models.BooleanField(_("Use Global template"), default=False)

    class Meta:
        verbose_name = _("Show Category")
        verbose_name_plural = _("Show Categories")

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ("shows_category", (), {
            "category_slug": self.slug,
        })


class Show(models.Model):
    """
    A TV show with title, description and photo
    """
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255)
    blurb = models.TextField(_("Blurb"), blank=True)
    description = models.TextField(_("Description"), blank=True)
    logo = models.ImageField(_("Logo"), upload_to="files/shows")
    photo = models.ImageField(_("Photo"), upload_to="files/shows", blank=True)
    category = models.ForeignKey(ShowCategory, verbose_name=_("Category"), related_name="shows")

    class Meta:
        verbose_name = _("Show")
        verbose_name_plural = _("Shows")

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ("shows_detail", (), {
            "category_slug": self.category.slug,
            "slug": self.slug,
        })

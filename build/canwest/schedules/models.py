from django.db import models
from django.utils.translation import ugettext_lazy as _


DAY_CHOICES = (
    ("monday", _("Monday")),
    ("tuesday", _("Tuesday")),
    ("wednesday", _("Wednesday")),
    ("thursday", _("Thursday")),
    ("friday", _("Friday")),
    ("saturday", _("Saturday")),
    ("sunday", _("Sunday")),
)


class ScheduledItem(models.Model):
    """
    An item in the schedule, tied to a specific day
    """
    title = models.CharField(_("Title"), max_length=255)
    start_time = models.TimeField(_("Start Time"))
    day = models.CharField(_("Day"), choices=DAY_CHOICES, max_length=10)

    class Meta:
        verbose_name = _("Scheduled Item")
        verbose_name_plural = _("Scheduled Items")

    def __unicode__(self):
        return u"%(title)s (%(time)s on %(day)s)" % {
            "title": self.title,
            "time": self.start_time.strftime("%H:%M"),
            "day": self.get_day_display(),
        }

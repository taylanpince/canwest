from django.db import models
from django.utils.translation import ugettext_lazy as _


DAY_CHOICES = (
    (0, _("Monday")),
    (1, _("Tuesday")),
    (2, _("Wednesday")),
    (3, _("Thursday")),
    (4, _("Friday")),
    (5, _("Saturday")),
    (6, _("Sunday")),
)


class ScheduleItem(models.Model):
    """
    An item in the schedule, tied to a specific day
    """
    title = models.CharField(_("Title"), max_length=255)
    start_time = models.TimeField(_("Start Time"))
    day = models.PositiveSmallIntegerField(_("Day"), choices=DAY_CHOICES)

    class Meta:
        verbose_name = _("Schedule Item")
        verbose_name_plural = _("Schedule Items")

    def __unicode__(self):
        return u"%(title)s (%(time)s on %(day)s)" % {
            "title": self.title,
            "time": self.start_time.strftime("%H:%M"),
            "day": self.get_day_display(),
        }

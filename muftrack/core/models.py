
# django modules
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FundCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)

    def __unicode__(self):
        return self.name


class Fund(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Fund Name"), unique=True, blank=False, db_index=True)
    category = models.ForeignKey(FundCategory, verbose_name=_("Fund Category"))
    aum = models.FloatField()  # Current Assests Under Management (in crores)

    def __unicode__(self):
        return self.name



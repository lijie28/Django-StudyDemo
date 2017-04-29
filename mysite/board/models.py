# from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Sprint(models.Model):
    """
    Description: Model Description
    """
    # name = models.CharFiedld(max_length=100, blank=True, default='')
    descripiton = models.TextField(blank=True, default='')
    # end = models.DataField(unique=True)

    def __str__(self):
        return self.name or _('Sprint ending %s') % self.end


class Task(models.Model):
    """
    Description: unit of work to be done for th sprint
    """
    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO, _('Not Started')),
        (STATUS_IN_PROGRESS, _('In Progress')),
        (STATUS_TESING, _('Testing')),
        (STATUS_DONE, _('Done')),
    )

    # name = models.CharFiedld(max_length=100)
    descripiton = models.TextField(blank=True, default='')
    sprint = models.ForeignKey(Sprint, blank=True, null=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)
    order = models.SmallIntegerField(default=0)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    # started = models.DataField(blank=True, null=True)
    # due = models.DataField(blank=True, null=True)
    # completed = models.DataField(blank=True, null=True)

    def __str__(self):
        return self.name


# class Spint(models.Model):
#     """
#     Description: Model Description
#     """
#     name = models.Charfiedld(max_length=100, blank=True, default='')
#     descripiton = models.TextField(blank=True, default='')
#     end = models.DataField(unique=True)

#     def __str__(self):
#         return self.name or _('Sprint ending %s') % self.end

    # class Meta:
    #     pass
# Create your models here.
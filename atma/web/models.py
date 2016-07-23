from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


STATUSES = (
    ('NS', 'Not started'),
    ('ON', 'Ongoing'),
    ('PO', 'Postponed'),
    ('AB', 'Aborted'),
    ('CO', 'Completed'),
)

PRIORITY_AREAS = (
    ('PR', 'Program'),
    ('IM', 'Impact'),
    ('EX', 'External recognition'),
    ('FU', 'Funding'),
    ('TA', 'Talent')
)


class PartnershipManager(User):

    points = models.IntegerField()


class Volunteer(User):

    points = models.IntegerField()


class NGO(models.Model):

    description = models.TextField()
    partnership_manager = models.OneToOneField(
        PartnershipManager,
        related_name='partnership_manager'
    )
    resources = models.TextField()
    status = models.CharField(max_length=2, choices=STATUSES)


class Strategy(models.Model):

    description = models.TextField()
    ngo = models.ForeignKey(NGO)
    year = models.IntegerField()
    status = models.CharField(max_length=2, choices=STATUSES)
    priority_area = models.CharField(max_length=2, choices=PRIORITY_AREAS)
    date_created = models.DateField(auto_now_add=True)
    deadline = models.DateField(auto_now_add=True)


class Project(models.Model):

    description = models.TextField()
    strategy = models.ForeignKey(Strategy)
    quarter = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    status = models.CharField(max_length=2, choices=STATUSES)
    assignee = models.OneToOneField(Volunteer)


class Task(models.Model):

    description = models.TextField()
    project = models.ForeignKey(Project)
    date_created = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    status = models.CharField(max_length=2, choices=STATUSES)


class Badges(models.Model):

    name = models.TextField()
    image_name = models.TextField()

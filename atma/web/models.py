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


class AtmaUserInfo(models.Model):

    user = models.OneToOneField(User)
    user_type = models.CharField(max_length=1,
                                 choices=(('V', 'Volunteers'),
                                          ('P', 'Project manager')))
    last_checked_in_time = models.DateField()
    streak = models.IntegerField()


class NGO(models.Model):

    name=models.TextField()
    sdescription = models.TextField()
    partnership_manager = models.ForeignKey(User,
                                            related_name='managers')
    resources = models.TextField()
    status = models.CharField(max_length=2, choices=STATUSES)

class Priority_Areas(models.Model):
    NGO_name=models.TextField()
    priority_area = models.CharField(max_length=20, choices=PRIORITY_AREAS)


class Strategy(models.Model):

    NGO_name=models.TextField()
    priority_name=models.TextField()
    strategy_name=models.TextField()
    description = models.TextField()
    ngo = models.ForeignKey(NGO)
    year = models.IntegerField()
    status = models.CharField(max_length=2, choices=STATUSES)

    date_created = models.DateField(auto_now_add=True)
    deadline = models.DateField(auto_now_add=True)

    def tasks_completed(self):
        # returns a tuple (completed, total)
        n_total = 0
        n_completed = 0
        for project in self.project_set.all():
            total = [len(x) for x in project.task_set.all()]
            n_total = n_total + total
            completed = filter(total, lambda x: x == 'CO')
            n_completed = n_completed + completed
        return (n_completed, n_total)


class Project(models.Model):
    NGO_name=models.TextField()
    description = models.TextField()
    strategy = models.ForeignKey(Strategy)
    quarter = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    status = models.CharField(max_length=2, choices=STATUSES)
    assignee = models.OneToOneField(User, related_name='assignee')

    def tasks_completed(self):
        # returns a tuple (completed, total)
        n_total = [len(x) for x in self.task_set.all()]
        n_completed = filter(n_total, lambda x: x == 'CO')
        return (n_completed, n_total)


class Task(models.Model):

    description = models.TextField()
    project = models.ForeignKey(Project)
    date_created = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    status = models.CharField(max_length=2, choices=STATUSES)


class Badges(models.Model):

    name = models.TextField()
    image_name = models.TextField()
    badge_type = models.CharField(max_length=1,
                                  choices=(('V', 'Volunteer'),
                                           ('P', 'Partnership manager')))


class OfficeLocation(models.Model):

    lat = models.FloatField()
    lng = models.FloatField()

# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Projects(models.Model):
    name = models.TextField()

class Tickets(models.Model):
    '''
    status  = {
        todo: "waiting to get started"
        working-on: "started and working on"
        finished: "the requested issue is resolved"
    }
    priority = {
        low: "low priority"
        normal: "moderate urgency"
        high: "high urgency"
        extreme: "extremely high urgency - have to be resolved as quick as posible"
    }
    '''
    header = models.TextField()
    priority = models.TextField()
    status = models.TextField(blank=True, default = "todo")
    createTime = models.DateTimeField(blank=True, default=datetime.datetime.now)
    comment = models.TextField(blank=True)
    createUserID = models.ForeignKey(User, related_name='createUser')
    modificationUserID = models.ForeignKey(User, default=None, blank=True, null=True, related_name='modificationUser')
    solveUserID = models.ForeignKey(User, blank=True, null=True, default=None, related_name='solveUser')
    projectID = models.ForeignKey(Projects)

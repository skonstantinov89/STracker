# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Tickets(models.Model):
    header = models.TextField()
    priority = models.TextField()
    createTime = models.DateTimeField(blank=True, default=datetime.datetime.now)
    createUserID = models.ForeignKey(User, related_name='createUser')
    modificationUserID = models.ForeignKey(User, default=None, blank=True, null=True, related_name='modificationUser')
    solveUserID = models.ForeignKey(User, blank=True, null=True, default=None, related_name='solveUser')

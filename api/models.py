from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

#!/usr/bin/python
# -*- coding: utf-8 -*-
class Question(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.CharField(max_length=600)
	subject = models.CharField(max_length=128)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.subject

	def __unicode__(self):
		return unicode(self.subject)

#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models

admin.site.register(models.Question)
# admin.site.register(models.Store)
# admin.site.register(models.Campaing)

#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index_view, name='Index'),
    url(r'^dashboard/$', views.dashboard_view, name='Dashboard Index'),

    url(r'^question/add/$', views.question_add, name='Add Question'),
    url(r'^question/edit/(?P<id>\d+)$', views.question_edit, name='Edit Question'),
    url(r'^question/delete/(?P<id>\d+)$', views.question_remove, name='Edit Question'),
    #
    # url(r'^store/add/$', views.stores_add, name='Add Store'),
    # url(r'^store/edit/(?P<id>\d+)$', views.stores_edit, name='Edit Store'),
    # url(r'^store/delete/(?P<id>\d+)$', views.stores_remove, name='Edit Store'),
    #
    # url(r'^campaing/add/$', views.campaing_add, name='Add Campaing'),
    # url(r'^campaing/edit/(?P<id>\d+)$', views.campaing_edit, name='Edit Campaing'),
    # url(r'^campaing/delete/(?P<id>\d+)$', views.campaing_remove, name='Edit Campaing'),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'secure/login.html'}),
    url(r'^logout/$', views.logout_view, name="Logout")
]

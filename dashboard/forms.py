#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from api.models import *

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('__all__')

	def __init__(self, user_id, *args, **kwargs):
		from django.forms.widgets import HiddenInput
		super(QuestionForm, self).__init__(*args, **kwargs)
		self.fields['user'].widget = HiddenInput()

#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from .forms import *
from api import models

from django.contrib.auth import logout

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index_view(request):
	return render(request, 'index.html',{})

def dashboard_view(request):
	if not request.user.is_authenticated():
		return redirect("/login")
	else:

		questionsList = models.Question.objects.all()
		questions = []
		for question in questionsList:
			questions.append({
				"subject": question.subject,
				"text": question.text,
				"id": question.id,
			})

		form=QuestionForm(request.user.id)
		return render(request, 'dashboard.html',{"user": request.user, "newQuestion": form.as_p(), "questions": questions})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('dashboard.views.index_view'))

######################
#QUESTIONS OPERATIONS#
######################

def question_add(request):
	if not request.user.is_authenticated():
		return redirect("/login")
	else:
		if request.method=="POST":
			data = request.POST.copy()
			data[u'user'] = unicode(request.user.id)
			form = QuestionForm(request.user.id,data)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('dashboard.views.dashboard_view'))
		else:
			form=QuestionForm(request.user.id)
		return render(request,'common/form.html',{'form':form.as_p(), "title": "Adicionar Nova pergunta"})

def question_edit(request,id):
	if not request.user.is_authenticated():
		return redirect("/login")
	else:
		if request.method=="POST":
			data = request.POST.copy()
			data[u'user'] = unicode(request.user.id)
			form = QuestionForm(request.user.id,data, instance=models.Question.objects.get(user_id=request.user.id, id=id))
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('dashboard.views.dashboard_view'))
		else:
			question = models.Question.objects.get(user_id=request.user.id, id=id)
			form=QuestionForm(request.user.id, instance=question)
		return render(request,'common/form.html',{'form':form.as_p(), "title": "Editar pergunta"})

def question_remove(request,id):
	if not request.user.is_authenticated():
		return redirect("/login")
	else:
		question = Question.objects.get(user_id=request.user.id, id=id)
		question.delete()
		return HttpResponseRedirect(reverse('dashboard.views.dashboard_view'))

#####################
#CAMPAING OPERATIONS#
#####################

def campaing_add(request):
	if not request.user.is_authenticated():
		return redirect("/dashboard/login")
	else:
		if request.method=="POST":
			data = request.POST.copy()
			data[u'user'] = unicode(request.user.id)
			form = CampaingForm(request.user.id,data)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('dashboard.views.index_view'))
		else:
			form=CampaingForm(request.user.id)
		return render(request,'common/form.html',{'form':form.as_p(), "title": "Adicionar Nova Campanha"})

def campaing_edit(request,id):
	if not request.user.is_authenticated():
		return redirect("/dashboard/login")
	else:
		if request.method=="POST":
			data = request.POST.copy()
			data[u'user'] = unicode(request.user.id)
			form = CampaingForm(request.user.id,data, instance=models.Campaing.objects.get(user_id=request.user.id, id=id))
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('dashboard.views.index_view'))
		else:
			campaing = models.Campaing.objects.get(user_id=request.user.id, id=id)
			form=CampaingForm(request.user.id, instance=campaing)
		return render(request,'common/form.html',{'form':form.as_p(), "title": "Editar Campanha \"" + campaing.card_title + "\""})

def campaing_remove(request,id):
	if not request.user.is_authenticated():
		return redirect("/dashboard/login")
	else:
		campaing = Campaing.objects.get(id=id)
		campaing.delete()
		return HttpResponseRedirect(reverse('dashboard.views.index_view'))

###################
#STORES OPERATIONS#
###################

def stores_add(request):
	if not request.user.is_authenticated():
		return redirect("/dashboard/login")
	else:
		if request.method=="POST":
			data = request.POST.copy()
			data[u'user'] = unicode(request.user.id)
			form = StoreForm(data)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('dashboard.views.index_view'))
		else:
			form=StoreForm()
		return render(request,'common/form.html',{'form':form.as_p(), "title": "Adicionar Nova Loja"})

def stores_edit(request,id):
	if not request.user.is_authenticated():
		return redirect("/dashboard/login")
	else:
		if request.method=="POST":
			data = request.POST.copy()
			data[u'user'] = unicode(request.user.id)
			form = StoreForm(data, instance=models.Store.objects.get(user_id=request.user.id, id=id))
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('dashboard.views.index_view'))
		else:
			store = models.Store.objects.get(user_id=request.user.id, id=id)
			form=StoreForm(instance=store)
		return render(request,'common/form.html',{'form':form.as_p(), "title": "Editar Loja \"" + store.name + "\""})

def stores_remove(request,id):
	if not request.user.is_authenticated():
		return redirect("/dashboard/login")
	else:
		store = Store.objects.get(user_id=request.user.id, id=id)
		store.delete()
		return HttpResponseRedirect(reverse('dashboard.views.index_view'))

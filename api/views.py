#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from . import models

import json

# def get_campaing(request,uid):
# 	try:
# 		beacon = models.Beacon.objects.get(uid=uid)
# 		store = beacon.store_id
# 		try:
# 			campaing = models.Campaing.objects.get(store_id = store)
# 			data = {
# 				"range": campaing.range,
# 				"card_media_url": campaing.card_media_url,
# 				"card_title": campaing.card_title,
# 				"card_content": campaing.card_content,
# 				"notification_title": campaing.notification_title,
# 				"notification_content": campaing.notification_content,
# 			}
# 			return HttpResponse(json.dumps(data))
# 		except Exception:
# 			return HttpResponse("{\"error\":\"no-campaing\"}")
# 	except Exception:
# 		return HttpResponse("{\"error\":\"no-beacon\"}")

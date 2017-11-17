# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from dataCalculator.models import *
from django.core import serializers
import json




db_manage = False
# Create your views here.
def tomainpage(request):
    all_elements = serializers.serialize("json", Element.objects.all())
    all_datastructrues = serializers.serialize("json", DataStructure.objects.all())

    context = {
        'elements': all_elements,
        'dataStructures': all_datastructrues,
        'dbManage': db_manage
    }

    return render(request, 'main.html',context)

def add_element_to_db(request):
    if(db_manage):
        element = json.loads(request.GET['element'])
        elementId = element['elementId']
        elementInfo = element['elementInfo']
        e = Element.objects.create(nodeId=elementId)
        for attr in elementInfo:
            setattr(e, str(attr), elementInfo[attr])
        e.save()
    return HttpResponse("")

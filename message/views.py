# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import UserMessage


# Create your views here.
def getform(request):
    # all_messages = UserMessage.objects.filter(name='bobby', address='北京')
    # for message in all_messages:
    #     print message.name
    user_message = UserMessage()
    user_message.name = "bobby2"
    user_message.message = "helloworld2"
    user_message.address = "上海"
    user_message.email = "2@2.com"
    user_message.object_id = "helloworld2"
    user_message.save()
    return render(request, 'message_form.html')

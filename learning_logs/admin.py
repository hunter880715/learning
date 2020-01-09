# -*- coding: utf-8 -*-
from django.contrib import admin
from learning_logs.models import Topic, Entry
# 在这里注册模型
admin.site.register(Topic)
admin.site.register(Entry)

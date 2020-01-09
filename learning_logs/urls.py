# coding: GBK
"""����learning_logs��URLģʽ"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # ��ҳ
    url(r'^topics/$', views.topics, name='topics'),
    # �ض��������ϸҳ��
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # ����������������ҳ
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # �����������Ŀ��ҳ��
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # ���ڱ༭��Ŀ��ҳ��
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, 
        name='edit_entry'),
]

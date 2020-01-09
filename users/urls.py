# coding: GBK 
"""ΪӦ�ó���users����URLģʽ"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    # ��¼ҳ��
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'),
        name='login'),
    # ע��
    url(r'^logout/$', views.logout_view, name='logout'),
    # ע��ҳ��
    url(r'^register/$', views.register, name='register'),
]

from django.conf.urls import url
from django.shortcuts import redirect
from rest_framework.urlpatterns import format_suffix_patterns
from restful import views

urlpatterns = [
    url(r'^files/(?P<path>(\/*[a-zA-z0-9가-힣._-]*/)*)$', views.FileList.as_view(), name='file-list'),
    url(r'^files/(?P<pk>[0-9]+)/$', views.FileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
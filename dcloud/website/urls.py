from django.conf.urls import url
from django.shortcuts import redirect
from website import views, auth_views

urlpatterns = [

    url(r'^accounts/signup/$', auth_views.signup, name='signup'),
    url(r'^accounts/delete_account/$', auth_views.delete_account, name='delete_account'),
    url(r'^accounts/delete_account_success/$', auth_views.delete_account_success, name='delete_account_success'),

    # blog
    url(r'^$', views.home),
    url(r'^files/', views.file_list, name='file_list'),
    url(r'^upload/', views.file_upload, name='file_upload'),
    url(r'^make_folder/', views.make_folder, name='make_folder'),

]
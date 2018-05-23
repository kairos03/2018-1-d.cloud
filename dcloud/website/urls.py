from django.conf.urls import url
from website import views, auth_views
from django.shortcuts import redirect

urlpatterns = [
    # blog
    url(r'^$', redirect('login')),
    url(r'^files/', views.file_list, name='file_list'),
    url(r'^accounts/signup/$', auth_views.signup, name='signup'),
    url(r'^accounts/delete_account/$', auth_views.delete_account, name='delete_account'),
    url(r'^accounts/delete_account_success/$', auth_views.delete_account_success, name='delete_account_success'),
]
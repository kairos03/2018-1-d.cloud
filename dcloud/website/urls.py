from django.conf.urls import url
from website import views, auth_views

urlpatterns = [
    # blog
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),

    url(r'^files/', views.file_list, name='file_list'),
    url(r'^signup/$', auth_views.signup, name='signup'),
]
from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^files/', views.file_list, name='file_list'),
    
]
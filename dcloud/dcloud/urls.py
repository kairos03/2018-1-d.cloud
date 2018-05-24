from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^restapi/', include('restful.urls')),
    url(r'^', include('website.urls')),

    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),

    url(r'^s3direct/', include('s3direct.urls')),
]


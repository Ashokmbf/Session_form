from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin


urlpatterns = [
    
    url(r'^$',views.user_detail_view,name='home'),
    url(r'^qualification/$',views.qualification_view,name='qualification_view'),
    url(r'^user_detail/$',views.user_detail_view,name='user_detail_view'),
    url(r'^preview/$',views.preview,name='preview'),
    # url(r'^qualifiation/$',views.qualification_view,name='qualification_view'),
]




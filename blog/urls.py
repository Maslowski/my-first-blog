from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
    url(r'^post/new/$', views.post_new, name = 'post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name = 'post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name = 'post_remove'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name = 'post_delete'),
    url(r'^all/$', views.post_list_all, name = 'post_list_all'),
]
"""
As you can see, we're now assigning a view called post_list to the ^$ URL. This regular expression will match ^ (a beginning) followed by $ (an end) – so only an empty string will match. That's correct, because in Django URL resolvers, 'http://127.0.0.1:8000/' is not a part of the URL. This pattern will tell Django that views.post_list is the right place to go if someone enters your website at the 'http://127.0.0.1:8000/' address.
"""

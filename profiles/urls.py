from django.conf.urls import patterns, include, url

from profiles.views import *

urlpatterns = patterns('',
    url(r'^$', MyProfileView.as_view(), name='my_profile'),
    url(r'^blog/$', MyBlogView.as_view(), name='my_blog'),
    url(r'^feeds/$', MyFeedsView.as_view(), name='my_feeds'),
    url(r'^tracks/$', MyTracksView.as_view(), name='my_tracks'),
    url(r'^projects/$', MyProjectsView.as_view(), name='my_projects'),
    url(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),
)

from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns(
	'django_eb.trialmanager.views',
	url(r'^$', views.index, name='index'),
    url(r'^profiles/$', 'profile_list', name='profile_list'),
    url(r'^greetings/$', 'greeting_list', name='greeting_list'),
    url(r'^(?P<profile_id>[0-9]+)/$', views.detail, name='detail')
)
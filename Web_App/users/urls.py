from django.conf.urls import patterns, url
from police import views

urlpatterns = patterns('',
	url(r'^authenticate/', 'users.views.login_user', name='authenticate'),
    
    url(r'^logout', 'users.views.logout_user', name='logout'),
    
    
    )
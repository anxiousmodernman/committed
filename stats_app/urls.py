from django.conf.urls import patterns, url
from stats_app import views

urlpatterns = patterns('stats_app.views',
    url(r'^$', views.stats, name='stats'),
)

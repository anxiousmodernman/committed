from django.conf.urls import include, url, patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('user.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/github', 'main.views.github_login'),
    url(r'^$', 'main.views.hello', name='committed_home')
)


# NOTE: we are taking the "more control" approach documented here:
# https://docs.djangoproject.com/en/1.8/topics/auth/default/#module-django.contrib.auth.views
urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login',
        {'template_name': 'login.html'},
        name='committed_login'),

    url(r'^logout/$', 'logout',
        {'next_page': 'committed_home'},
        name='committed_logout'),
)

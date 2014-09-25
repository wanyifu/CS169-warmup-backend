from django.conf.urls import patterns, include, url


from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/login$', 'polls.views.login'),
    url(r'^users/add$', 'polls.views.add'),
    url(r'^TESTAPI/resetFixture$', 'polls.views.reset'),
    url(r'^TESTAPI/unitTests$', 'polls.views.test'),
)

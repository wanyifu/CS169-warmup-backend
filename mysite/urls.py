from django.conf.urls import patterns, include, url


from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'polls.views.renderer'),
    # url(r'^frontend.css$',TemplateView.as_view(template_name='frontend.css'))
    url(r'^users/login$', 'polls.views.login'),
    url(r'^users/add$', 'polls.views.add'),
    url(r'^TESTAPI/resetFixture$', 'polls.views.TESTAPI_resetFixture'),
    url(r'^TESTAPI/unitTests$', 'polls.views.TESTAPI_unitTests'),
    #url(r'^$',TemplateView.as_view(template_name='frontend.html'), name="bla")
    
)

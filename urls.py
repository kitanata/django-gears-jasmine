from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'ci$', 'jasmine.views.jasmine_ci', name='jasmine-ci'),
    url(r'^$', 'jasmine.views.jasmine', name='jasmine')
)

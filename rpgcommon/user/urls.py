from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('rpgcommon.user.views',
    url("^registrace/$", 'inviteform', {'template' : 'registration/inviteform.html'}, name="inviteform"),
)

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('rpgcommon.user.views',
    url("^registrace/$", 'inviteform', {'template' : 'registration/inviteform.html'}, name="inviteform"),
    url("^prihlaseni/$", 'login', {'template' : 'registration/login.html'}, name="login"),
    url("^odhlasit/$", 'logout', {'template' : 'registration/logout.html'}, name="logout"),
)

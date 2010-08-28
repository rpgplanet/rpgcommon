from django.contrib.sites.models import Site
from django.http import Http404
from django.conf import settings

from urlparse import urlparse

import facebook

from rpgcommon.user.models import FacebookAccount

class FbAutoLoginMiddleware:
    def process_request(self, request):
        if not request.user.is_authenticated():
            fb_info = facebook.get_user_from_cookie(request.COOKIES, settings.FACEBOOK_APPLICATION_ID, settings.FACEBOOK_APPLICATION_SECRET)
            if fb_info:
                queryargs = {}
                for fb_key, model_key in (
                    ("uid", "facebook_uid"),
                ):
                    queryargs.update({model_key : fb_info[fb_key]})

                try:
                    account = FacebookAccount.objects.get(**queryargs)
                except FacebookAccount.DoesNotExist:
                    pass
                else:
                    from django.contrib.auth import authenticate, login
                    user = authenticate(facebook_uid=account.facebook_uid)
                    if user and user.is_active:
                        login(request, user)

            
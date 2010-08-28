
from copy import copy
from hashlib import md5
from time import time
from urllib import urlencode

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

import facebook

from rpgcommon.user.models import UserProfile
from rpgcommon.service.utils import unixize_name


def create_user(username, password, email):
    user = User.objects.create_user(
        username = username,
        email = email,
        password = password
    )

    slug = unixize_name(username)

    home = "%s.rpghrac.cz" % slug

    site = Site.objects.create(
        domain = home,
        name = home
    )

    UserProfile.objects.create(
        slug = slug,
        user = user,
        site = site
    )

    return user

def logout(request):
    from django.contrib.auth import logout as django_logout
    django_logout(request)


def fb_logout(cookies, response):
    fb_info = facebook.get_user_from_cookie(cookies, settings.FACEBOOK_APPLICATION_ID, settings.FACEBOOK_APPLICATION_SECRET)
    if fb_info:
        fb_info['uid'] = ""
        fb_info['access_token'] = ""

        ###########
        ### just reverse facebook.get_user_from_cookie.
        ### Original get_user_from_cookie is from Facebook Python SDK
        ### Copyright 2010 Facebook
        ### Licensed under the Apache License, Version 2.0 (the "License")
        ### Modified for set by Almad
        ##########

        response['P3P'] = 'CP="NOI DSP COR NID ADMa OPTa OUR NOR"'
        
        expire_time = time() - 86400

        args = copy(fb_info)
        args['expires'] = str(int(expire_time))
        payload = "".join([k + "=" + fb_info[k] for k in sorted(args.keys()) if k != "sig"])
        
        args['sig'] = md5(payload+settings.FACEBOOK_APPLICATION_SECRET).hexdigest()

        response.set_cookie('fbs_%s' % settings.FACEBOOK_APPLICATION_ID , urlencode(args), expires=expire_time)


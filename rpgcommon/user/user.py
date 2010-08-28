from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

import facebook

from time import time

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


###########
### set_fb_cookie and cookie_signature taken from Facebook Python SDK examples
### Copyright 2010 Facebook
### Licensed under the Apache License, Version 2.0 (the "License")
### See http://github.com/facebook/python-sdk/blob/master/examples/oauth/facebookoauth.py
### Modified for Django usage by Almad
##########
def cookie_signature(*parts):
    """Generates a cookie signature.

    We use the Facebook app secret since it is different for every app (so
    people using this example don't accidentally all use the same secret).
    """
    import hashlib
    import hmac
    hash = hmac.new(settings.FACEBOOK_APPLICATION_SECRET, digestmod=hashlib.sha1)
    for part in parts: hash.update(part)
    return hash.hexdigest()

def set_fb_cookie(response, name, value, domain=None, path="/", expires=None):
    """Generates and signs a cookie for the give name/value"""
    import base64
    import Cookie
    import email.utils
    
    timestamp = str(int(time()))
    value = base64.b64encode(value)
    signature = cookie_signature(value, timestamp)
    cookie = Cookie.BaseCookie()
    cookie[name] = "|".join([value, timestamp, signature])
    cookie[name]["path"] = path
    if domain: cookie[name]["domain"] = domain
    if expires:
        cookie[name]["expires"] = email.utils.formatdate(
            expires, localtime=False, usegmt=True)
    response["Set-Cookie"] = cookie.output()[12:]

def fb_logout(cookies, response):
    fb_info = facebook.get_user_from_cookie(cookies, settings.FACEBOOK_APPLICATION_ID, settings.FACEBOOK_APPLICATION_SECRET)
    if fb_info:
        set_fb_cookie(response, "fb_user", "", expires=time() - 86400)



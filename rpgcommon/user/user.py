
from copy import copy
from hashlib import md5
from time import time
from urllib import urlencode

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from ella.core.models import Category

import facebook

from rpgcommon.user.models import UserProfile
from rpgcommon.service.utils import unixize_name

# categories that will be created immediatelly after user creation
# they MUST be given in order of dependence ("rpg" first, "rpg/drd" second).
# "" (root category) is automagic
DEFAULT_USER_MANDATORY_CATEGORIES = [
    "rpg"
]

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


    # hm, rpgcommon shall not depend on rpghrac...
    from rpghrac.zapisnik.zapisnik import Zapisnik
    zapisnik = Zapisnik(owner=user, site=site)
    root = zapisnik.root_category

    categories = [cat for cat in settings.DYNAMIC_RPGPLAYER_CATEGORIES if cat['tree_path'] in getattr(settings, "USER_MANDATORY_DYNAMIC_CATEGORIES", None) or DEFAULT_USER_MANDATORY_CATEGORIES]

    for category_dict in categories:
        if category_dict['tree_path']:
            parent = root
        else:
            Category.objects.get(tree_path=category_dict['tree_path'])
            
        Category.objects.create(
            site = site,
            tree_path = category_dict['tree_path'],
            tree_parent = parent,
            title = category_dict['title'],
            slug = category_dict['slug']
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

        response.set_cookie('fbs_%s' % settings.FACEBOOK_APPLICATION_ID , urlencode(args), expires=expire_time, domain=settings.SESSION_COOKIE_DOMAIN)


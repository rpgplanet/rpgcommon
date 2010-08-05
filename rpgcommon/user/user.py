from django.contrib.auth.models import User
from django.contrib.sites.models import Site

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

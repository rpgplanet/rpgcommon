from django.db.models import (
    Model,
    CharField,
    ForeignKey,
)

from django.contrib.auth.models import User
from django.contrib.sites.models import Site

class UserProfile(Model):
    user = ForeignKey(User, unique=True)
    slug = CharField(max_length=50, unique=True)
    site = ForeignKey(Site, unique=True)

class InvitedEmail(Model):
    email = CharField(max_length=50, unique=True)

from django.db.models import (
    Model,
    CharField, TextField, DateTimeField,
    ForeignKey,
)

from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from anyjson import serialize, deserialize

class UserProfile(Model):
    user = ForeignKey(User, unique=True)
    slug = CharField(max_length=50, unique=True)
    site = ForeignKey(Site, unique=True)

class InvitedEmail(Model):
    email = CharField(max_length=50, unique=True)

class FacebookAccount(Model):
    user = ForeignKey(User, unique=True)
    facebook_uid = CharField(max_length=30, unique=True)
    access_token = CharField(max_length=255, unique=True)
    expires = DateTimeField()
    secret = CharField(max_length=50, unique=True)
    signature = CharField(max_length=50)
    session_key = CharField(max_length=255)
    data = TextField()

    def get_json_data(self):
        return deserialize(self.data)

    def set_json_data(self, data):
        self.data = serialize(data)
        return self.data

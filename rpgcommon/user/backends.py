from django.contrib.auth.models import User

from rpgcommon.user.models import FacebookAccount

class FacebookBackend(object):
    def authenticate(self, facebook_uid=None, **kwargs):
        if facebook_uid:
            try:
                return FacebookAccount.objects.get(facebook_uid=facebook_uid).user
            except FacebookAccount.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
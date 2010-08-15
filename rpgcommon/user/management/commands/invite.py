from django.core.management.base import BaseCommand

from rpgcommon.user.models import InvitedEmail

class Command(BaseCommand):
    args = '<email email ...>'
    help = 'Invite given email(s)'

    def handle(self, *args, **options):
        for email in args:
            InvitedEmail.objects.create(email=email)


from django.core.management.base import NoArgsCommand
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify

from ella.core.models import Category

class Command(NoArgsCommand):
    help = '''fix categories on rpg hrac (create missing)'''
    
    def handle(self, *args, **options):

        categories = settings.DYNAMIC_RPGPLAYER_CATEGORIES

        #TODO: batching & slicing?
        users = User.objects.all()

        for user in users:
            try:
                site = Site.objects.get(domain="%s.rpghrac.cz" % slugify(user.username))
            except Site.DoesNotExist:
                print "Not site for user %s (%s)!" % (slugify(user.username), str(user))

            for category in categories:
                try:
                    Category.objects.get_or_create(
                        site = site,
                        tree_path = category['tree_path'],
                        tree_parent = Category.objects.get(site=site, tree_path=category['parent_tree_path']),
                        title = category['title'],
                        slug = category['slug']
                    )
                except Category.DoesNotExist:
                    print "No root category for user %s!" % slugify(user.username)



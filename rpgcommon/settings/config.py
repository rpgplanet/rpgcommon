# -*- coding: utf-8 -*-
from os.path import dirname, join, pardir, abspath

import rpgcommon

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ENABLE_DEBUG_URLS = DEBUG

DATABASE_ENGINE="mysql"
DATABASE_NAME="rpgplanet"
DATABASE_USER="developer"
DATABASE_PASSWORD="xxx"

FILE_ROOT = dirname(rpgcommon.__file__)


# Make this unique, and don't share it with anybody.
SECRET_KEY = '88b-01f^x$%&^*&(&$)^*(U(8798756786(*bbbBBBndasdf)93!0#k(=mfv$'


MEDIA_ROOT = join(FILE_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = join(FILE_ROOT, 'static')
STATIC_URL = '/static/'


ADMIN_MEDIA_PREFIX = '/static/admin_media/'
NEWMAN_MEDIA_PREFIX = '/static/newman_media/'

# init logger
LOGGING_CONFIG_FILE = join(FILE_ROOT, 'settings', 'logging.ini')

CACHE_BACKEND = 'dummy://'

TEST_MEDIA_ROOT = abspath(join(FILE_ROOT, pardir, 'tests', 'data'))

# should be set to None for production
TEST_MEDIA_URL = "/test/media/"

LOGGING_CONFIG_FILE = join(dirname(__file__), 'logging.ini')

DYNAMIC_RPGPLAYER_CATEGORIES = [
#    {
#        "tree_path" : "",
#        "parent_tree_path" : "",
#        "title" : u"",
#        "slug" : "",
#    },
    {
        "tree_path" : "rpg",
        "parent_tree_path" : "",
        "title" : u"RPG",
        "slug" : "rpg",
    },
    {
        "tree_path" : "rpg/draci-doupe",
        "parent_tree_path" : "rpg",
        "title" : u"Dračí Doupě",
        "slug" : "draci-doupe",
    },


    {
        "tree_path" : "rpg/drd2",
        "parent_tree_path" : "rpg",
        "title" : u"Dračí Doupě II",
        "slug" : "draci-doupe-2",
    },


    {
        "tree_path" : "rpg/dnd3",
        "parent_tree_path" : "rpg",
        "title" : u"Dungeons & Dragons v. 3.5",
        "slug" : "dnd3",
    },
    {
        "tree_path" : "rpg/dnd3/povolani",
        "parent_tree_path" : "rpg/dnd3",
        "title" : u"Rubrika Povolání (Classes)",
        "slug" : "povolani",
    },
    {
        "tree_path" : "rpg/dnd3/povolani/zakladni",
        "parent_tree_path" : "rpg/dnd3/povolani",
        "title" : u"Základní povolání (Classes)",
        "slug" : "zakladni",
    },
    {
        "tree_path" : "rpg/dnd3/povolani/prestizni",
        "parent_tree_path" : "rpg/dnd3/povolani",
        "title" : u"Prestižní povolání (Prestige Classes)",
        "slug" : "prestizni",
    },
    {
        "tree_path" : "rpg/dnd3/povolani/epicke",
        "parent_tree_path" : "rpg/dnd3/povolani",
        "title" : u"Epické povolání (Epic Classes)",
        "slug" : "epicke",
    },
    {
        "tree_path" : "rpg/dnd3/odbornosti",
        "parent_tree_path" : "rpg/dnd3",
        "title" : u"Rubrika Odbornosti (Feats)",
        "slug" : "odbornosti",
    },
    {
        "tree_path" : "rpg/dnd3/odbornosti/obecne",
        "parent_tree_path" : "rpg/dnd3/odbornosti",
        "title" : u"Obecné odbornosti (General Feats)",
        "slug" : "obecne",
    },
    {
        "tree_path" : "rpg/dnd3/odbornosti/metamagicke",
        "parent_tree_path" : "rpg/dnd3/odbornosti",
        "title" : u"Metamagické odbornosti (Metamagic Feats)",
        "slug" : "metamagicke",
    },
    {
        "tree_path" : "rpg/dnd3/odbornosti/vyrobni",
        "parent_tree_path" : "rpg/dnd3/odbornosti",
        "title" : u"Výrobní odbornosti (Item Creation Feats)",
        "slug" : "vyrobni",
    },
    {
        "tree_path" : "rpg/dnd3/odbornosti/epicke",
        "parent_tree_path" : "rpg/dnd3/odbornosti",
        "title" : u"Epické odbornosti (Epic Feats)",
        "slug" : "epicke",
    },
    {
        "tree_path" : "rpg/dnd3/odbornosti/bestii",
        "parent_tree_path" : "rpg/dnd3/odbornosti",
        "title" : u"Odbornosti bestií (Monster Feats)",
        "slug" : "bestii",
    },
    {
        "tree_path" : "rpg/dnd3/predmety",
        "parent_tree_path" : "rpg/dnd3",
        "title" : u"Předměty (Items)",
        "slug" : "predmety",
    },
    {
        "tree_path" : "rpg/dnd3/predmety/obycejne",
        "parent_tree_path" : "rpg/dnd3/predmety",
        "title" : u"Obyčejné předměty (General Items)",
        "slug" : "obycejne",
    },
    {
        "tree_path" : "rpg/dnd3/predmety/magicke",
        "parent_tree_path" : "rpg/dnd3/predmety",
        "title" : u"Magické předměty (Wondrous Items)",
        "slug" : "magicke",
    },
    {
        "tree_path" : "rpg/dnd3/predmety/artefakty-a-relikvie",
        "parent_tree_path" : "rpg/dnd3/predmety",
        "title" : u"Artefakty a relikvie",
        "slug" : "artefakty-a-relikvie",
    },
    {
        "tree_path" : "rpg/dnd3/predmety/materialy",
        "parent_tree_path" : "rpg/dnd3/predmety",
        "title" : u"Materiály",
        "slug" : "materialy",
    },
    {
        "tree_path" : "rpg/dnd3/bestiar",
        "parent_tree_path" : "rpg/dnd3",
        "title" : u"Bestiář (Monster manual)",
        "slug" : "bestiar",
    },
    {
        "tree_path" : "rpg/dnd3/monsters/rasy",
        "parent_tree_path" : "rpg/dnd3/bestiar",
        "title" : u"Rasy (PC Races)",
        "slug" : "rasy",
    },
    {
        "tree_path" : "rpg/dnd3/monsters/postavy",
        "parent_tree_path" : "rpg/dnd3/bestiar",
        "title" : u"Postavy (NPC)",
        "slug" : "postavy",
    },
    {
        "tree_path" : "rpg/dnd3/kouzla",
        "parent_tree_path" : "rpg/dnd3",
        "title" : u"Kouzla (Spells)",
        "slug" : "kouzla",
    },
    {
        "tree_path" : "rpg/dnd3/kouzla/klericke-domeny",
        "parent_tree_path" : "rpg/dnd3/kouzla",
        "title" : u"Klericke domény (Cleric Domains)",
        "slug" : "klericke-domeny",
    },
    {
        "tree_path" : "rpg/dnd3/kouzla/epicka-kouzla",
        "parent_tree_path" : "rpg/dnd3/kouzla",
        "title" : u"Epické kouzla (Epic Spells)",
        "slug" : "epicka-kouzla",
    },
    {
        "tree_path" : "rpg/dnd3/kouzla/psionicka-kouzla",
        "parent_tree_path" : "rpg/dnd3/kouzla",
        "title" : u"Psionická kouzla (Psionic Powers)",
        "slug" : "psionicka-kouzla",
    },
    {
        "tree_path" : "rpg/dnd3/dobrodruzstvi",
        "parent_tree_path" : "rpg/dnd3",
        "title" : u"Dobrodružství",
        "slug" : "dobrodruzstvi",
    },
    {
        "tree_path" : "rpg/dnd3/dobrodruzstvi/setkani",
        "parent_tree_path" : "rpg/dnd3/dobrodruzstvi",
        "title" : u"Stkání (Encounters)",
        "slug" : "setkání",
    },
    {
        "tree_path" : "rpg/dnd3/dobrodruzstvi/kampane",
        "parent_tree_path" : "rpg/dnd3/dobrodruzstvi",
        "title" : u"Kampaně (Campaigns)",
        "slug" : "kampane",
    },
    {
        "tree_path" : "rpg/dnd3/dobrodruzstvi/popis-sveta",
        "parent_tree_path" : "rpg/dnd3/dobrodruzstvi",
        "title" : u"Popis světa",
        "slug" : "popis-sveta",
    },
    {
        "tree_path" : "rpg/dnd3/pravidla",
        "parent_tree_path" : "rpg/dnd3",
        "title" : u"Ostatní pravidla",
        "slug" : "pravidla",
    },
    {
        "tree_path" : "rpg/dnd3/pravidla/dovednosti",
        "parent_tree_path" : "rpg/dnd3/pravidla",
        "title" : u"Dovednosti (Skills)",
        "slug" : "dovednosti",
    },
    {
        "tree_path" : "rpg/dnd3/pravidla/alternativni",
        "parent_tree_path" : "rpg/dnd3/pravidla",
        "title" : u"Alternativní pravidla",
        "slug" : "alternativní",
    },
    {
        "tree_path" : "rpg/dnd3/pravidla/rozvoj-dnd",
        "parent_tree_path" : "rpg/dnd3/pravidla",
        "title" : u"Rozvoj DnD3.5",
        "slug" : "rozvoj-dnd",
    },
    {
        "tree_path" : "rpg/dnd3/ostatni",
        "parent_tree_path" : "rpg/dnd3",
        "title" : u"Ostatní",
        "slug" : "ostatni",
    },
    {
        "tree_path" : "rpg/dnd3/rest/beletrie",
        "parent_tree_path" : "rpg/dnd3/rest",
        "title" : u"Beletrie v Dnd",
        "slug" : "beletrie",
    },
]


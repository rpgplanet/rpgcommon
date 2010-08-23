import re
from unicodedata import normalize
from unicodedata import combining

from django.shortcuts import render_to_response
from django.template import RequestContext

def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)

def undiacritic(text, encoding='utf-8'):
    if type(text) == type(''):
        text = unicode(text, encoding)
    text = normalize('NFKD', text)
    text = [char for char in text if not combining(char)]
    text = ''.join(text)
    return text

def unixize_name(name):
    """ Return name in unix format (= national characters and special chars stripped) """
    unixname = undiacritic(name)
    unixname = unixname.lower()
    unixname = re.sub("[ ]", "-", unixname)
    unixname = re.sub("([-]+)", "-", unixname)
    unixname = re.sub("([_]+)", "-", unixname)
    unixname = re.sub("^([^a-z])+", "", unixname)
    unixname = re.sub("([^a-z]+)$", "", unixname)
    return unixname

def urlize(s):
    """ Return URLized string (= only characters alowed in URL retrieed)"""
    unixname = undiacritic(s)
    unixname = unixname.lower()
    unixname = re.sub("[^a-z0-9]+", "-", unixname)
    unixname = re.sub("^([^a-z0-9])+", "", unixname)
    unixname = re.sub("([^a-z0-9]+)$", "", unixname)
    return unixname

def urlized_path(path):
    """ Return path with all parts urlized() """
    if type(path) == type(''):
        path = path.decode('utf-8')
    s = ''.join([u''.join([urlize(path_part), u'/']) for path_part in path.split(u'/')])[:-1]
    if not s.endswith(u'/'):
        s = ''.join([s, u'/'])
    return s

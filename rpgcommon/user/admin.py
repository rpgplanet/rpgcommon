"""
This code aims to override the username's regex of the Django admin panel to be
able to allow unicode usernames.

Copied from http://diegobz.net/wp-content/uploads/2009/11/admin.txt and modified.
"""

import re
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

help_text = _("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.")

error_message = _("This value must contain only unicode letters, "
                  "numbers and underscores.")


class UnicodeRegexField(forms.RegexField):
    """
    Return a regex field that allows unicode chars.

    The ``regex`` parameter needs to be a basestring for that to happen.
    """
    def __init__(self, regex, max_length=None, min_length=None,
        error_message=None, *args, **kwargs):

        if isinstance(regex, basestring):
            # Here it's the trick
            regex = re.compile(regex, re.UNICODE)

        super(UnicodeRegexField, self).__init__(regex, max_length,
            min_length, *args, **kwargs)


class UserCreationForm(UserCreationForm):
    # The regex must be a string
    username = UnicodeRegexField(label=_("Username"), max_length=30,
        regex=u'^[\w ]+$', help_text=help_text, error_message=error_message)


class UserChangeForm(UserChangeForm):
    # The regex must be a string
    username = UnicodeRegexField(label=_("Username"), max_length=30,
        regex=u'^[\w ]+$', help_text=help_text, error_message=error_message)


class UserProfileAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)

# -*- coding: utf-8 -*-

from datetime import datetime
import warnings

from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.forms import (
    Form, ValidationError,
    CharField, EmailField,
    PasswordInput
)

from django.views.generic.simple import direct_to_template

import facebook

from rpgcommon.user.models import InvitedEmail, FacebookAccount
from rpgcommon.user.user import create_user


class RegistrationForm(Form):
    username = CharField(label="Uživatelské jméno", max_length=30)
    email = EmailField()
    password = CharField(label="Heslo", widget=PasswordInput)
    password_confirm = CharField(label="Potvrzení hesla", widget=PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("email", "")

        try:
            User.objects.get(email=email)
            raise ValidationError("Tento e-mail je již registrován")
        except User.DoesNotExist:
            pass

        try:
            InvitedEmail.objects.get(email=email)
        except InvitedEmail.DoesNotExist, err:
            raise ValidationError(u"Na tento e-mail není dostupná žádná pozvánka. Omlouváme se - poprostě někoho registrovaného, nebo se přijďte podívat později!")

        return email
        
    def clean_password_confirm(self):
        password = self.cleaned_data.get("password", "")
        password_confirm = self.cleaned_data["password_confirm"]
        if password != password_confirm:
            raise ValidationError("Hesla nejsou stejná. Prosím, upravte svůj překlep.")
        return password_confirm

    def clean_username(self):
        #TODO
        return self.cleaned_data.get("username", "")


class FacebookForm(Form):
    username = CharField(label="Uživatelské jméno", max_length=30)

def inviteform(request, template='registration/inviteform.html'):
    message = ''
    
    if request.POST.get("traditional_registration", None):
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user = create_user(
                username = registration_form.cleaned_data['username'],
                password = registration_form.cleaned_data['password'],
                email = registration_form.cleaned_data['email']
            )

            return HttpResponseRedirect(reverse('service:profile', kwargs={
                "user_slug" : user.get_profile().slug
            }))
    else:
        registration_form = RegistrationForm()

    if not getattr(settings, "FACEBOOK_APPLICATION_ID", None) or not getattr(settings, "FACEBOOK_APPLICATION_SECRET", None):
        warnings.warn("FACEBOOK_APPLICATION_ID or FACEBOOK_APPLICATION_SECRET not given, not handling FB authentication")

    if request.POST.get("facebook_registration", None):
        fb_form = FacebookForm(request.POST)
        fb_form.visible = True

        if fb_form.is_valid():
            if not getattr(settings, "FACEBOOK_APPLICATION_ID", None) or not getattr(settings, "FACEBOOK_APPLICATION_SECRET", None):
                message = u"Aplikace bohužel nemá k dispozici nastavení potřebná na používání s Facebookem :-/"
            else:
                fb_info = facebook.get_user_from_cookie(request.COOKIES, settings.FACEBOOK_APPLICATION_ID, settings.FACEBOOK_APPLICATION_SECRET)

                if not fb_info:
                    message = u"Nepodařilo se získat informace z Facebooku. Má problémy? Nebo došlo k chybě při přenosu informací? Zkuste to znovu."
                else:
                    graph = facebook.GraphAPI(fb_info["access_token"])
                    profile = graph.get_object("me")
        #            friends = graph.get_connections("me", "friends")

                    if 'email' not in profile:
                        message = u"Neposkytl jsi mi e-mail, ale já ho skutečně potřebuji pro fungování. Prosím odhlaš se z Facebook a tentokrát mi ho poskytni :o)"
                    else:
                        try:
                            InvitedEmail.objects.get(email=profile['email'])
                        except InvitedEmail.DoesNotExist, err:
                            message = u"Na tento e-mail není dostupná žádná pozvánka. Omlouváme se - poprostě někoho registrovaného, nebo se přijďte podívat později!"
                        else:
                            # finally, we can create profile
                            user = create_user(
                                username = fb_form.cleaned_data['username'],
                                password = '',
                                email = profile['email']
                            )

                            account = FacebookAccount(
                                user = user
                            )

                            for fb_key, model_key in (
                                ("uid", "facebook_uid"),
                                ("access_token", "access_token"),
                                ("secret", "secret"),
                                ("sig", "signature"),
                                ("session_key", "session_key"),
                            ):
                                setattr(account, model_key, fb_info[fb_key])

                            account.expires = datetime.utcfromtimestamp(float(fb_info['expires']))

                            account.set_json_data(profile)

                            account.save()

                            return HttpResponseRedirect(reverse('service:profile', kwargs={
                                "user_slug" : user.get_profile().slug
                            }))

    else:
        fb_form = FacebookForm()
        fb_form.visible = False

    return direct_to_template(request, template, {
        'registration_form' : registration_form,
        'fb_form' : fb_form,
        'message' : message,
    })

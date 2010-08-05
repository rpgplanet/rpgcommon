# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.forms import (
    Form, ValidationError,
    CharField, EmailField,
    PasswordInput
)

from django.views.generic.simple import direct_to_template

from rpgcommon.user.models import InvitedEmail
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


def inviteform(request, template='registration/inviteform.html'):
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
    
    return direct_to_template(request, template, {
        'registration_form' : registration_form,
    })

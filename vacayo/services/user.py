from django.apps import apps
from django.conf import settings
from django.contrib.auth import authenticate, login
from allauth.utils import generate_unique_username
from allauth.account.models import EmailAddress
from ..models import Owner, Host, Location, Lead

User = apps.get_model(settings.AUTH_USER_MODEL, require_ready=True)


class UserService(object):

    def __init__(self):
        pass

    def get(self, email):
        return User.objects.filter(email=email).first()

    def create(self, first_name, last_name, email, password1, password2, *args, **kwargs):
        assert not User.objects.filter(email=email).exists()

        user = User()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.set_password(password1)
        user.username = generate_unique_username([first_name, last_name, email, None, 'user'])
        user.save()

        # needed for django-allauth
        EmailAddress(user=user, email=email, primary=True, verified=False).save()

        return user

    def login(self, request, username, password):
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

        return user

    def assign_owner_role(self, user, phone, *args, **kwargs):
        owner, _ = Owner.objects.get_or_create(
            user=user,
            phone=phone
        )

        return owner

    def assign_host_role(self, user):
        host, _ = Host.objects.get_or_create(
            user=user,
            defaults={
                'location': Location.objects.create()
            }
        )

        return host

    def record_lead(self, address, first_name, last_name, email, phone, *args, **kwargs):
        location = Location.objects.create(
            address=address
        )

        lead = Lead.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            location=location
        )

        return lead

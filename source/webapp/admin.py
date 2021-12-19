from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from webapp.models import Client

admin.site.register(Client)

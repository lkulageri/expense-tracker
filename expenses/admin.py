# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from expenses.models import UserProfileInfo, User
# Register your models here.

admin.site.register(UserProfileInfo)
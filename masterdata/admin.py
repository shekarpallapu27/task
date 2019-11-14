
from django.contrib import admin

# Register your models here.

from django.contrib import admin
from masterdata.models import *
# Register your models here.
from django.apps import apps
from .models import *




for i in apps.all_models['masterdata'].values():
    admin.site.register(i)
from django.contrib import admin

# Register your models here.
from django.contrib.admin.decorators import register

from .models import snacks

admin.site.register(snacks)
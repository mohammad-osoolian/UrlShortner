from django.contrib import admin
from .models import *


class UrlAdmin(admin.ModelAdmin):
    fields = ['url',  'key', 'created']
    readonly_fields = ['created', 'key']
    list_display = ['id', 'key', 'created']


admin.site.register(Url, UrlAdmin)

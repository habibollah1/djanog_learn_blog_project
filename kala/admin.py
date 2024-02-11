from django.contrib import admin
from .models import KalaList


class KalaAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified', 'author')
    ordering = ('-status',)


admin.site.register(KalaList, KalaAdmin)

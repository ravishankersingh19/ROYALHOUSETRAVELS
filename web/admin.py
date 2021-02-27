from django.contrib import admin

# Register your models here.

from .models import (
    location,
    Subcriber,
    contact,
    Setting,
)

class LocationAdmin(admin.ModelAdmin):
    pass

class SubcriberAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

class SettingAdmin(admin.ModelAdmin):
    pass

admin.site.register(location,LocationAdmin)
admin.site.register(Subcriber,SubcriberAdmin)
admin.site.register(contact,ContactAdmin)
admin.site.register(Setting,SettingAdmin)


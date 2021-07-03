from django.contrib import admin

from .models import Contact, Tool, TravelPhoto
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    readonly_fields = ["created",]

@admin.register(TravelPhoto)
class TravelPhotoAdmin(admin.ModelAdmin):
    pass

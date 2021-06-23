from django.contrib import admin

from .models import Contact, Tool
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    readonly_fields = ["created",]

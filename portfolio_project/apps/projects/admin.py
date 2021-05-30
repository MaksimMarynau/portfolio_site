from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','description','technology','image_tag')

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100", height=auto />'.format(obj.image.url))

    image_tag.short_description = 'Image'

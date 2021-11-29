from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Project, ProjectImages

class ProjectImagesAdmin(admin.StackedInline):
    model = ProjectImages
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','description','image_tag')
    filter_horizontal = ('tool_used',)
    inlines = [ProjectImagesAdmin]

    class Meta:
        model = Project

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100", height=auto />'.format(obj.image.url))

    image_tag.short_description = 'Image'

@admin.register(ProjectImages)
class ProjectImagesAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

# Register your models here.
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','last_modified')
    filter_horizontal = ('categories',)
    fieldsets = (
        (None, {
        	'fields':('title','categories',)
        }),
        (None, {
        	'fields':('body',)
        }),
        )

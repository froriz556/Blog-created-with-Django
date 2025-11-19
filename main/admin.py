from django.contrib import admin
from unicodedata import category

from .models import Category, Post

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_categories', 'is_published', 'time_create', 'time_update', 'text_content', 'image')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-time_create',)
    readonly_fields = ('time_create', 'time_update')
    search_fields = ('title', 'text_content')
    list_filter = ('author', 'categories', 'is_published')

    def get_categories(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all()])

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', )

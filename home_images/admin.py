from django.contrib import admin

from .models import HomeImage


class HomeAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'image',
        'caption',
        'order'
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'caption',)
    list_display = ('title', 'order',)
    list_editable = ('order',)

admin.site.register(HomeImage, HomeAdmin)
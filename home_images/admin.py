from django.contrib import admin

from .models import HomeImage


class HomeAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'image',
        'caption',
        'display_order',
        'parallax'
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'caption',)
    list_display = ('title', 'display_order', 'parallax')
    list_editable = ('display_order', 'parallax')

admin.site.register(HomeImage, HomeAdmin)
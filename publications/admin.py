from django.contrib import admin
from django.urls import reverse

from .models import PressRelease, Publication, Work, WorkPicture
from .support_models import Category, Medium, Program, Status


class WorkPictureInline(admin.StackedInline):
    model = WorkPicture
    extra = 1
    prepopulated_fields = {'slug': ('title',)}

class WorkAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'description',
        'category',
        'program',
        'status',
        'published_date',
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category', 'program', 'status',)
    list_filter = ('created_date', 'category', 'program', 'status',)
    list_display = ('title', 'category', 'program', 'status', 'published_date', '_is_published',)
    list_editable = ('category', 'status', 'program', 'published_date',)
    inlines = [WorkPictureInline]


class WorkPictureAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'image',
        'caption',
        'work',
        'is_cover',
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('work', 'title',)
    list_filter = ('work',)
    list_display = ('title', 'work', 'is_cover',)
    list_editable = ('work', 'is_cover',)


class PublicationAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'description',
        'image',
        'category',
        'published_date',
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category',)
    list_filter = ('created_date', 'category',)
    list_display = ('title', 'category', 'medium', 'published_date', '_is_published',)
    list_editable = ('category','medium', 'published_date',)


class PressReleaseAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'description',
        'url',
        'category',
        'published_date',
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category',)
    list_filter = ('created_date', 'category',)
    list_display = ('title', 'category', 'published_date', '_is_published',)
    list_editable = ('category', 'published_date',)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    
class MediumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

class StatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

class ProgramAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)



admin.site.register(Work, WorkAdmin)
admin.site.register(PressRelease, PressReleaseAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WorkPicture, WorkPictureAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Medium, MediumAdmin)


admin.site.site_header = "Estudio Caribe Administration"